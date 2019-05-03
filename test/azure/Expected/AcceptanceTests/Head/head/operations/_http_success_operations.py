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

import uuid
from azure.core.exceptions import HttpResponseError, map_error


class HttpSuccessOperations(object):
    """HttpSuccessOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self._config = config

    def head200(self, cls=None, **kwargs):
        """Return 200 status code if successful.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: bool or the result of cls(response)
        :rtype: bool
        :raises: :class:`HttpResponseError<azure.core.HttpResponseError>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.head200.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = (response.status_code == 200)
        return deserialized
    head200.metadata = {'url': '/http/success/200'}

    def head204(self, cls=None, **kwargs):
        """Return 204 status code if successful.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: bool or the result of cls(response)
        :rtype: bool
        :raises: :class:`HttpResponseError<azure.core.HttpResponseError>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.head204.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = (response.status_code == 204)
        return deserialized
    head204.metadata = {'url': '/http/success/204'}

    def head404(self, cls=None, **kwargs):
        """Return 404 status code if successful.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: bool or the result of cls(response)
        :rtype: bool
        :raises: :class:`HttpResponseError<azure.core.HttpResponseError>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.head404.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = (response.status_code == 204)
        return deserialized
    head404.metadata = {'url': '/http/success/404'}
