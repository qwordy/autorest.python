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


from .. import models


class QueriesOperations(object):
    """QueriesOperations operations.

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

    def array_string_multi_null(self, array_query=None, cls=None, **kwargs):
        """Get a null array of string using the multi-array format.

        :param array_query: a null array of string using the multi-array
         format
        :type array_query: list[str]
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<urlmulticollectionformat.models.ErrorException>`
        """
        # Construct URL
        url = self.array_string_multi_null.metadata['url']

        # Construct parameters
        query_parameters = {}
        if array_query is not None:
            query_parameters['arrayQuery'] = self._serialize.query("array_query", array_query, '[str]', div=',')

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    array_string_multi_null.metadata = {'url': '/queries/array/multi/string/null'}

    def array_string_multi_empty(self, array_query=None, cls=None, **kwargs):
        """Get an empty array [] of string using the multi-array format.

        :param array_query: an empty array [] of string using the multi-array
         format
        :type array_query: list[str]
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<urlmulticollectionformat.models.ErrorException>`
        """
        # Construct URL
        url = self.array_string_multi_empty.metadata['url']

        # Construct parameters
        query_parameters = {}
        if array_query is not None:
            query_parameters['arrayQuery'] = self._serialize.query("array_query", array_query, '[str]', div=',')

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    array_string_multi_empty.metadata = {'url': '/queries/array/multi/string/empty'}

    def array_string_multi_valid(self, array_query=None, cls=None, **kwargs):
        """Get an array of string ['ArrayQuery1', 'begin!*'();:@ &=+$,/?#[]end' ,
        null, ''] using the mult-array format.

        :param array_query: an array of string ['ArrayQuery1', 'begin!*'();:@
         &=+$,/?#[]end' , null, ''] using the mult-array format
        :type array_query: list[str]
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<urlmulticollectionformat.models.ErrorException>`
        """
        # Construct URL
        url = self.array_string_multi_valid.metadata['url']

        # Construct parameters
        query_parameters = {}
        if array_query is not None:
            query_parameters['arrayQuery'] = self._serialize.query("array_query", array_query, '[str]', div=',')

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    array_string_multi_valid.metadata = {'url': '/queries/array/multi/string/valid'}