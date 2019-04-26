# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from azure.core import HttpRequestError


class Error(Model):
    """Error.

    :param code:
    :type code: int
    :param message:
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class ErrorException(HttpRequestError):
    """Server responsed with exception of type: 'Error'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, response, deserialize, *args):

      model_name = 'Error'
      self.error = deserialize(model_name, response)
      if self.error is None:
          self.error = deserialize.dependencies[model_name]()
      super(ErrorException, self).__init__(response=response)


class HttpRequestError(Model):
    """HttpRequestError.
    """

    _attribute_map = {
    }


class SampleResourceGroup(Model):
    """SampleResourceGroup.

    :param name: resource group name 'testgroup101'
    :type name: str
    :param location: resource group location 'West US'
    :type location: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SampleResourceGroup, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.location = kwargs.get('location', None)