# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class HeaderOperations:
    """HeaderOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azurespecialproperties.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def _custom_named_request_id_request(self, foo_client_request_id: str, **kwargs) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = self._custom_named_request_id_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["foo-client-request-id"] = self._serialize.header(
            "foo_client_request_id", foo_client_request_id, "str"
        )
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.post(url, query_parameters, header_parameters)

    _custom_named_request_id_request.metadata = {"url": "/azurespecials/customNamedRequestId"}  # type: ignore

    @distributed_trace_async
    async def custom_named_request_id(self, foo_client_request_id: str, **kwargs) -> None:
        """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in the header of the request.

        :param foo_client_request_id: The fooRequestId.
        :type foo_client_request_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._custom_named_request_id_request(foo_client_request_id=foo_client_request_id, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["foo-request-id"] = self._deserialize("str", response.headers.get("foo-request-id"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    custom_named_request_id.metadata = {"url": "/azurespecials/customNamedRequestId"}  # type: ignore

    def _custom_named_request_id_param_grouping_request(
        self,
        header_custom_named_request_id_param_grouping_parameters: "_models.HeaderCustomNamedRequestIdParamGroupingParameters",
        **kwargs
    ) -> HttpRequest:

        _foo_client_request_id = None
        if header_custom_named_request_id_param_grouping_parameters is not None:
            _foo_client_request_id = header_custom_named_request_id_param_grouping_parameters.foo_client_request_id
        accept = "application/json"

        # Construct URL
        url = self._custom_named_request_id_param_grouping_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["foo-client-request-id"] = self._serialize.header(
            "foo_client_request_id", _foo_client_request_id, "str"
        )
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.post(url, query_parameters, header_parameters)

    _custom_named_request_id_param_grouping_request.metadata = {"url": "/azurespecials/customNamedRequestIdParamGrouping"}  # type: ignore

    @distributed_trace_async
    async def custom_named_request_id_param_grouping(
        self,
        header_custom_named_request_id_param_grouping_parameters: "_models.HeaderCustomNamedRequestIdParamGroupingParameters",
        **kwargs
    ) -> None:
        """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in the header of the request,
        via a parameter group.

        :param header_custom_named_request_id_param_grouping_parameters: Parameter group.
        :type header_custom_named_request_id_param_grouping_parameters: ~azurespecialproperties.models.HeaderCustomNamedRequestIdParamGroupingParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._custom_named_request_id_param_grouping_request(
            header_custom_named_request_id_param_grouping_parameters=header_custom_named_request_id_param_grouping_parameters,
            **kwargs
        )
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["foo-request-id"] = self._deserialize("str", response.headers.get("foo-request-id"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    custom_named_request_id_param_grouping.metadata = {"url": "/azurespecials/customNamedRequestIdParamGrouping"}  # type: ignore

    def _custom_named_request_id_head_request(self, foo_client_request_id: str, **kwargs) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = self._custom_named_request_id_head_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["foo-client-request-id"] = self._serialize.header(
            "foo_client_request_id", foo_client_request_id, "str"
        )
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.head(url, query_parameters, header_parameters)

    _custom_named_request_id_head_request.metadata = {"url": "/azurespecials/customNamedRequestIdHead"}  # type: ignore

    @distributed_trace_async
    async def custom_named_request_id_head(self, foo_client_request_id: str, **kwargs) -> bool:
        """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in the header of the request.

        :param foo_client_request_id: The fooRequestId.
        :type foo_client_request_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bool, or the result of cls(response)
        :rtype: bool
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._custom_named_request_id_head_request(foo_client_request_id=foo_client_request_id, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            response_headers["foo-request-id"] = self._deserialize("str", response.headers.get("foo-request-id"))

        if cls:
            return cls(pipeline_response, None, response_headers)
        return 200 <= response.status_code <= 299

    custom_named_request_id_head.metadata = {"url": "/azurespecials/customNamedRequestIdHead"}  # type: ignore
