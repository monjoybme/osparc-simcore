# coding: utf-8

"""
    simcore-service-storage API

    API definition for simcore-service-storage service  # noqa: E501

    OpenAPI spec version: 0.1.0
    Contact: support@simcore.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class FakeType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'path_value': 'str',
        'query_value': 'str',
        'body_value': 'dict(str, str)'
    }

    attribute_map = {
        'path_value': 'path_value',
        'query_value': 'query_value',
        'body_value': 'body_value'
    }

    def __init__(self, path_value=None, query_value=None, body_value=None):  # noqa: E501
        """FakeType - a model defined in OpenAPI"""  # noqa: E501

        self._path_value = None
        self._query_value = None
        self._body_value = None
        self.discriminator = None

        self.path_value = path_value
        self.query_value = query_value
        self.body_value = body_value

    @property
    def path_value(self):
        """Gets the path_value of this FakeType.  # noqa: E501


        :return: The path_value of this FakeType.  # noqa: E501
        :rtype: str
        """
        return self._path_value

    @path_value.setter
    def path_value(self, path_value):
        """Sets the path_value of this FakeType.


        :param path_value: The path_value of this FakeType.  # noqa: E501
        :type: str
        """
        if path_value is None:
            raise ValueError("Invalid value for `path_value`, must not be `None`")  # noqa: E501

        self._path_value = path_value

    @property
    def query_value(self):
        """Gets the query_value of this FakeType.  # noqa: E501


        :return: The query_value of this FakeType.  # noqa: E501
        :rtype: str
        """
        return self._query_value

    @query_value.setter
    def query_value(self, query_value):
        """Sets the query_value of this FakeType.


        :param query_value: The query_value of this FakeType.  # noqa: E501
        :type: str
        """
        if query_value is None:
            raise ValueError("Invalid value for `query_value`, must not be `None`")  # noqa: E501

        self._query_value = query_value

    @property
    def body_value(self):
        """Gets the body_value of this FakeType.  # noqa: E501


        :return: The body_value of this FakeType.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._body_value

    @body_value.setter
    def body_value(self, body_value):
        """Sets the body_value of this FakeType.


        :param body_value: The body_value of this FakeType.  # noqa: E501
        :type: dict(str, str)
        """
        if body_value is None:
            raise ValueError("Invalid value for `body_value`, must not be `None`")  # noqa: E501

        self._body_value = body_value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FakeType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
