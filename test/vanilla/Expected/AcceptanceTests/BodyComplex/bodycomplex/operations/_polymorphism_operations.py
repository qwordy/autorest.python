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


class PolymorphismOperations(object):
    """PolymorphismOperations operations.

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

    def get_valid(self, cls=None, **kwargs):
        """Get complex types that are polymorphic.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: Fish or the result of cls(response)
        :rtype: ~bodycomplex.models.Fish
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_valid.metadata['url']

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
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Fish', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_valid.metadata = {'url': '/complex/polymorphism/valid'}

    def put_valid(self, complex_body, cls=None, **kwargs):
        """Put complex types that are polymorphic.

        :param complex_body: Please put a salmon that looks like this:
         {
         'fishtype':'Salmon',
         'location':'alaska',
         'iswild':true,
         'species':'king',
         'length':1.0,
         'siblings':[
         {
         'fishtype':'Shark',
         'age':6,
         'birthday': '2012-01-05T01:00:00Z',
         'length':20.0,
         'species':'predator',
         },
         {
         'fishtype':'Sawshark',
         'age':105,
         'birthday': '1900-01-05T01:00:00Z',
         'length':10.0,
         'picture': new Buffer([255, 255, 255, 255, 254]).toString('base64'),
         'species':'dangerous',
         },
         {
         'fishtype': 'goblin',
         'age': 1,
         'birthday': '2015-08-08T00:00:00Z',
         'length': 30.0,
         'species': 'scary',
         'jawsize': 5
         }
         ]
         };
        :type complex_body: ~bodycomplex.models.Fish
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.put_valid.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(complex_body, 'Fish')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    put_valid.metadata = {'url': '/complex/polymorphism/valid'}

    def get_complicated(self, cls=None, **kwargs):
        """Get complex types that are polymorphic, but not at the root of the
        hierarchy; also have additional properties.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: Salmon or the result of cls(response)
        :rtype: ~bodycomplex.models.Salmon
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_complicated.metadata['url']

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
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Salmon', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_complicated.metadata = {'url': '/complex/polymorphism/complicated'}

    def put_complicated(self, complex_body, cls=None, **kwargs):
        """Put complex types that are polymorphic, but not at the root of the
        hierarchy; also have additional properties.

        :param complex_body:
        :type complex_body: ~bodycomplex.models.Salmon
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.put_complicated.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(complex_body, 'Salmon')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    put_complicated.metadata = {'url': '/complex/polymorphism/complicated'}

    def put_missing_discriminator(self, complex_body, cls=None, **kwargs):
        """Put complex types that are polymorphic, omitting the discriminator.

        :param complex_body:
        :type complex_body: ~bodycomplex.models.Salmon
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: Salmon or the result of cls(response)
        :rtype: ~bodycomplex.models.Salmon
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.put_missing_discriminator.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(complex_body, 'Salmon')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Salmon', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    put_missing_discriminator.metadata = {'url': '/complex/polymorphism/missingdiscriminator'}

    def put_valid_missing_required(self, complex_body, cls=None, **kwargs):
        """Put complex types that are polymorphic, attempting to omit required
        'birthday' field - the request should not be allowed from the client.

        :param complex_body: Please attempt put a sawshark that looks like
         this, the client should not allow this data to be sent:
         {
         "fishtype": "sawshark",
         "species": "snaggle toothed",
         "length": 18.5,
         "age": 2,
         "birthday": "2013-06-01T01:00:00Z",
         "location": "alaska",
         "picture": base64(FF FF FF FF FE),
         "siblings": [
         {
         "fishtype": "shark",
         "species": "predator",
         "birthday": "2012-01-05T01:00:00Z",
         "length": 20,
         "age": 6
         },
         {
         "fishtype": "sawshark",
         "species": "dangerous",
         "picture": base64(FF FF FF FF FE),
         "length": 10,
         "age": 105
         }
         ]
         }
        :type complex_body: ~bodycomplex.models.Fish
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.put_valid_missing_required.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(complex_body, 'Fish')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    put_valid_missing_required.metadata = {'url': '/complex/polymorphism/missingrequired/invalid'}