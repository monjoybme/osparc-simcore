"""this module is responsible for JSON encoding/decoding of nodeports objects."""
import json
import logging

from simcore_sdk.nodeports import nodeports #pylint: disable=cyclic-import
from simcore_sdk.nodeports._itemslist import DataItemsList
from simcore_sdk.nodeports._item import DataItem
from simcore_sdk.nodeports import exceptions
from simcore_sdk.nodeports import config
from simcore_sdk.models.pipeline_models import ComputationalTask as NodeModel

_LOGGER = logging.getLogger(__name__)

def create_from_json(io_obj, auto_read=False, auto_write=False):
    """creates a Nodeports object provided a json configuration in form of a callback function.
    
    Arguments:
        io_obj {object} -- interface object to connect to nodeports description.
    
    Keyword Arguments:
        auto_read {bool} -- the nodeports object shall automatically update itself when set to True (default: {False})
        auto_write {bool} -- the nodeports object shall automatically write the new outputs when set to True (default: {False})
    
    Raises:
        exceptions.NodeportsException -- raised in case of io object is empty
    
    Returns:
        object -- the Nodeports object
    """

    _LOGGER.debug("Creating Nodeports object with io object: %s, auto read %s and auto write %s", io_obj, auto_read, auto_write)
    if not io_obj:
        raise exceptions.NodeportsException("io object empty, this is not allowed")
    nodeports_obj = json.loads(io_obj.get_ports_configuration(), object_hook=nodeports_decoder)
    nodeports_obj.io_obj = io_obj
    nodeports_obj.autoread = auto_read
    nodeports_obj.autowrite = auto_write
    _LOGGER.debug("Created Nodeports object")
    return nodeports_obj

def create_nodeports_from_uuid(io_obj, node_uuid):
    _LOGGER.debug("Creating Nodeports object from node uuid: %s", node_uuid)
    if not io_obj:
        raise exceptions.NodeportsException("Invalid call to create nodeports from uuid")
    nodeports_obj = json.loads(io_obj.get_ports_configuration_from_node_uuid(node_uuid), object_hook=nodeports_decoder)
    _LOGGER.debug("Created Nodeports object")
    return nodeports_obj

def save_to_json(nodeports_obj):
    """encodes a Nodeports object to json and calls a linked writer if available.
    
    Arguments:
        nodeports_obj {Nodeports} -- the object to encode
    """

    auto_update_state = nodeports_obj.autoread
    try:
        # dumping triggers a load of unwanted auto-updates
        # which do not make sense for saving purpose.
        nodeports_obj.autoread = False
        nodeports_json = json.dumps(nodeports_obj, cls=_NodeportsEncoder)
    finally:
        nodeports_obj.autoread = auto_update_state
    
    if nodeports_obj.autowrite:
        nodeports_obj.io_obj.write_ports_configuration(nodeports_json)
    _LOGGER.info("Saved Nodeports object to json: %s", nodeports_json)

class _NodeportsEncoder(json.JSONEncoder):
    # SAN: looks like pylint is having an issue here
    def default(self, o): # pylint: disable=E0202
        _LOGGER.debug("Encoding object: %s", o)
        if isinstance(o, nodeports.Nodeports):
            _LOGGER.debug("Encoding Nodeports object")
            return {
                "version": o._version, # pylint: disable=W0212
                "inputs": o.inputs, # pylint: disable=W0212
                "outputs": o.outputs # pylint: disable=W0212
            }
        elif isinstance(o, DataItemsList):
            _LOGGER.debug("Encoding DataItemsList object")
            items = [data_item._asdict() for data_item in o]
            return items
        _LOGGER.debug("Encoding object using defaults")
        return json.JSONEncoder.default(self, o)
    
def nodeports_decoder(dct):
    """JSON decoder for Nodeports objects.
    
    Arguments:
        dct {dictionary} -- represents json configuration of a Nodeports object
    
    Raises:
        exceptions.InvalidProtocolError -- if the protocol is not recognized
    
    Returns:
        Nodeports,DataItemsList,DataItem -- objects necessary for a complete JSON decoding
    """
    _LOGGER.debug(dct)
    if "version" in dct and "inputs" in dct and "outputs" in dct:
        _LOGGER.debug("Decoding Nodeports json: %s", dct)
        return nodeports.Nodeports(dct["version"], DataItemsList(dct["inputs"]), DataItemsList(dct["outputs"]))
    
    # check for dataitem
    #TODO: SAN this is not good. decoding objects going bottom/up seems strange
    for key in config.DATA_ITEM_KEYS:
        if key == "timestamp": # optional
            continue
        if key not in dct:
            return dct
            #raise exceptions.InvalidProtocolError(dct, "key \"%s\" is missing" % (str(key)))
    _LOGGER.debug("Decoding Data items json: %s", dct)
    return DataItem(**dct)

def save_node_to_json(node):
    node_json_config = json.dumps(node, cls=_NodeModelEncoder)
    return node_json_config

def create_node_from_json(json_config):
    node = json.loads(json_config, object_hook=nodemodel_decoder)
    return node

class _NodeModelEncoder(json.JSONEncoder):
    def default(self, o): # pylint: disable=E0202
        _LOGGER.debug("Encoding object: %s", o)
        if isinstance(o, NodeModel):
            _LOGGER.debug("Encoding Node object")
            return {"version": "0.1", #TODO: SAN this will need to be correctly read
                    "inputs": o.input, 
                    "outputs": o.output
                    }
            # return {"version": o.tag, 
            #         "inputs": o.inputs, 
            #         "outputs": o.outputs
            #         }
        _LOGGER.debug("Encoding object using defaults")
        return json.JSONEncoder.default(self, o)

def nodemodel_decoder(dct):
    if "version" in dct and "inputs" in dct and "outputs" in dct:
        _LOGGER.debug("Decoding Nodeports json: %s", dct)
        return NodeModel(input=dct["inputs"], output=dct["outputs"])
        #return NodeModel(tag=dct["version"], inputs=dct["inputs"], outputs=dct["outputs"])
    # for key in config.DATA_ITEM_KEYS:
    #     if key not in dct:
    #         raise exceptions.InvalidProtocolError(dct)
    # _LOGGER.debug("Decoding Data items json: %s", dct)
    return dct