# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from .base_model_ import Model
from .inline_response2003_data import InlineResponse2003Data
from .. import util


class InlineResponse201(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: InlineResponse2003Data=None, error: object=None):
        """InlineResponse201 - a model defined in OpenAPI

        :param data: The data of this InlineResponse201.
        :param error: The error of this InlineResponse201.
        """
        self.openapi_types = {
            'data': InlineResponse2003Data,
            'error': object
        }

        self.attribute_map = {
            'data': 'data',
            'error': 'error'
        }

        self._data = data
        self._error = error

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InlineResponse201':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The inline_response_201 of this InlineResponse201.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this InlineResponse201.


        :return: The data of this InlineResponse201.
        :rtype: InlineResponse2003Data
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse201.


        :param data: The data of this InlineResponse201.
        :type data: InlineResponse2003Data
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def error(self):
        """Gets the error of this InlineResponse201.


        :return: The error of this InlineResponse201.
        :rtype: object
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this InlineResponse201.


        :param error: The error of this InlineResponse201.
        :type error: object
        """

        self._error = error
