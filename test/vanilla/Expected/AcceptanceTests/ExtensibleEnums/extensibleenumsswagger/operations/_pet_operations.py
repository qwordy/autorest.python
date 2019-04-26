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

from azure.core import HttpRequestError

from .. import models


class PetOperations(object):
    """PetOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self._config = config

    def get_by_pet_id(self, pet_id, cls=None, **kwargs):
        """

        :param pet_id: Pet id
        :type pet_id: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: Pet or the result of cls(response)
        :rtype: ~extensibleenumsswagger.models.Pet
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.get_by_pet_id.metadata['url']
        path_format_arguments = {
            'petId': self._serialize.url("pet_id", pet_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Pet', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_by_pet_id.metadata = {'url': '/extensibleenums/pet/{petId}'}

    def add_pet(self, pet_param=None, cls=None, **kwargs):
        """

        :param pet_param:
        :type pet_param: ~extensibleenumsswagger.models.Pet
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: Pet or the result of cls(response)
        :rtype: ~extensibleenumsswagger.models.Pet
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.add_pet.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        if pet_param is not None:
            body_content = self._serialize.body(pet_param, 'Pet')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Pet', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    add_pet.metadata = {'url': '/extensibleenums/pet/addPet'}