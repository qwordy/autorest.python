# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models

T = TypeVar('T')
ClsReturnType = TypeVar('ClsReturnType')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], ClsReturnType]]

class HttpRedirectsOperations:
    """HttpRedirectsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~httpinfrastructure.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def head300(
        self,
        **kwargs
    ) -> Optional[ClsReturnType]:
        """Return 300 status code and redirect to /http/success/200.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None, ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.head300.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 300]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 300:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

        return None
    head300.metadata = {'url': '/http/redirect/300'}  # type: ignore

    @distributed_trace_async
    async def get300(
        self,
        **kwargs
    ) -> Union[Optional[List[str]], ClsReturnType]:
        """Return 300 status code and redirect to /http/success/200.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of str, or the result of cls(response)
        :rtype: list[str] or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional[List[str]], ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get300.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 300]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        deserialized = None
        if response.status_code == 300:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
            deserialized = self._deserialize('[str]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get300.metadata = {'url': '/http/redirect/300'}  # type: ignore

    @distributed_trace_async
    async def head301(
        self,
        **kwargs
    ) -> Optional[ClsReturnType]:
        """Return 301 status code and redirect to /http/success/200.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None, ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.head301.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 301]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 301:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

        return None
    head301.metadata = {'url': '/http/redirect/301'}  # type: ignore

    @distributed_trace_async
    async def get301(
        self,
        **kwargs
    ) -> Optional[ClsReturnType]:
        """Return 301 status code and redirect to /http/success/200.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None, ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get301.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 301]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 301:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

        return None
    get301.metadata = {'url': '/http/redirect/301'}  # type: ignore

    @distributed_trace_async
    async def put301(
        self,
        boolean_value: Optional[bool] = True,
        **kwargs
    ) -> Optional[ClsReturnType]:
        """Put true Boolean value in request returns 301.  This request should not be automatically
        redirected, but should return the received 301 to the caller for evaluation.

        :param boolean_value: Simple boolean value true.
        :type boolean_value: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None, ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.put301.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [301]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

        return None
    put301.metadata = {'url': '/http/redirect/301'}  # type: ignore

    @distributed_trace_async
    async def head302(
        self,
        **kwargs
    ) -> Optional[ClsReturnType]:
        """Return 302 status code and redirect to /http/success/200.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None, ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.head302.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 302]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 302:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

        return None
    head302.metadata = {'url': '/http/redirect/302'}  # type: ignore

    @distributed_trace_async
    async def get302(
        self,
        **kwargs
    ) -> Optional[ClsReturnType]:
        """Return 302 status code and redirect to /http/success/200.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None, ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get302.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 302]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 302:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

        return None
    get302.metadata = {'url': '/http/redirect/302'}  # type: ignore

    @distributed_trace_async
    async def patch302(
        self,
        boolean_value: Optional[bool] = True,
        **kwargs
    ) -> Optional[ClsReturnType]:
        """Patch true Boolean value in request returns 302.  This request should not be automatically
        redirected, but should return the received 302 to the caller for evaluation.

        :param boolean_value: Simple boolean value true.
        :type boolean_value: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None, ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.patch302.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [302]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

        return None
    patch302.metadata = {'url': '/http/redirect/302'}  # type: ignore

    @distributed_trace_async
    async def post303(
        self,
        boolean_value: Optional[bool] = True,
        **kwargs
    ) -> Optional[ClsReturnType]:
        """Post true Boolean value in request returns 303.  This request should be automatically
        redirected usign a get, ultimately returning a 200 status code.

        :param boolean_value: Simple boolean value true.
        :type boolean_value: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None, ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.post303.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 303]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 303:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

        return None
    post303.metadata = {'url': '/http/redirect/303'}  # type: ignore

    @distributed_trace_async
    async def head307(
        self,
        **kwargs
    ) -> Optional[ClsReturnType]:
        """Redirect with 307, resulting in a 200 success.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None, ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.head307.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

        return None
    head307.metadata = {'url': '/http/redirect/307'}  # type: ignore

    @distributed_trace_async
    async def get307(
        self,
        **kwargs
    ) -> Optional[ClsReturnType]:
        """Redirect get with 307, resulting in a 200 success.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None, ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get307.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

        return None
    get307.metadata = {'url': '/http/redirect/307'}  # type: ignore

    @distributed_trace_async
    async def options307(
        self,
        **kwargs
    ) -> Optional[ClsReturnType]:
        """options redirected with 307, resulting in a 200 after redirect.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None, ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.options307.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.options(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

        return None
    options307.metadata = {'url': '/http/redirect/307'}  # type: ignore

    @distributed_trace_async
    async def put307(
        self,
        boolean_value: Optional[bool] = True,
        **kwargs
    ) -> Optional[ClsReturnType]:
        """Put redirected with 307, resulting in a 200 after redirect.

        :param boolean_value: Simple boolean value true.
        :type boolean_value: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None, ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.put307.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

        return None
    put307.metadata = {'url': '/http/redirect/307'}  # type: ignore

    @distributed_trace_async
    async def patch307(
        self,
        boolean_value: Optional[bool] = True,
        **kwargs
    ) -> Optional[ClsReturnType]:
        """Patch redirected with 307, resulting in a 200 after redirect.

        :param boolean_value: Simple boolean value true.
        :type boolean_value: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None, ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.patch307.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

        return None
    patch307.metadata = {'url': '/http/redirect/307'}  # type: ignore

    @distributed_trace_async
    async def post307(
        self,
        boolean_value: Optional[bool] = True,
        **kwargs
    ) -> Optional[ClsReturnType]:
        """Post redirected with 307, resulting in a 200 after redirect.

        :param boolean_value: Simple boolean value true.
        :type boolean_value: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None, ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.post307.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

        return None
    post307.metadata = {'url': '/http/redirect/307'}  # type: ignore

    @distributed_trace_async
    async def delete307(
        self,
        boolean_value: Optional[bool] = True,
        **kwargs
    ) -> Optional[ClsReturnType]:
        """Delete redirected with 307, resulting in a 200 after redirect.

        :param boolean_value: Simple boolean value true.
        :type boolean_value: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None, ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.delete307.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.delete(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

        return None
    delete307.metadata = {'url': '/http/redirect/307'}  # type: ignore
