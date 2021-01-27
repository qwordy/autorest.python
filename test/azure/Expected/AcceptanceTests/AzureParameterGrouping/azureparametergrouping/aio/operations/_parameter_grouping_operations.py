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

from ... import models as _models

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ParameterGroupingOperations:
    """ParameterGroupingOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azureparametergrouping.models
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

    def _post_required_request(
        self, parameter_grouping_post_required_parameters: "_models.ParameterGroupingPostRequiredParameters", **kwargs
    ) -> HttpRequest:

        _custom_header = None
        _query = None
        _path = None
        _body = None
        if parameter_grouping_post_required_parameters is not None:
            _custom_header = parameter_grouping_post_required_parameters.custom_header
            _query = parameter_grouping_post_required_parameters.query
            _path = parameter_grouping_post_required_parameters.path
            _body = parameter_grouping_post_required_parameters.body
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._post_required_request.metadata["url"]  # type: ignore
        path_format_arguments = {
            "path": self._serialize.url("path", _path, "str"),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if _query is not None:
            query_parameters["query"] = self._serialize.query("query", _query, "int")

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _custom_header is not None:
            header_parameters["customHeader"] = self._serialize.header("custom_header", _custom_header, "str")
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, "int")
        body_content_kwargs["content"] = body_content
        return self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

    _post_required_request.metadata = {"url": "/parameterGrouping/postRequired/{path}"}  # type: ignore

    @distributed_trace_async
    async def post_required(
        self, parameter_grouping_post_required_parameters: "_models.ParameterGroupingPostRequiredParameters", **kwargs
    ) -> None:
        """Post a bunch of required parameters grouped.

        :param parameter_grouping_post_required_parameters: Parameter group.
        :type parameter_grouping_post_required_parameters: ~azureparametergrouping.models.ParameterGroupingPostRequiredParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._post_required_request(
            parameter_grouping_post_required_parameters=parameter_grouping_post_required_parameters, **kwargs
        )
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    post_required.metadata = {"url": "/parameterGrouping/postRequired/{path}"}  # type: ignore

    def _post_optional_request(
        self,
        parameter_grouping_post_optional_parameters: Optional["_models.ParameterGroupingPostOptionalParameters"] = None,
        **kwargs
    ) -> HttpRequest:

        _custom_header = None
        _query = None
        if parameter_grouping_post_optional_parameters is not None:
            _custom_header = parameter_grouping_post_optional_parameters.custom_header
            _query = parameter_grouping_post_optional_parameters.query
        accept = "application/json"

        # Construct URL
        url = self._post_optional_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if _query is not None:
            query_parameters["query"] = self._serialize.query("query", _query, "int")

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _custom_header is not None:
            header_parameters["customHeader"] = self._serialize.header("custom_header", _custom_header, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.post(url, query_parameters, header_parameters)

    _post_optional_request.metadata = {"url": "/parameterGrouping/postOptional"}  # type: ignore

    @distributed_trace_async
    async def post_optional(
        self,
        parameter_grouping_post_optional_parameters: Optional["_models.ParameterGroupingPostOptionalParameters"] = None,
        **kwargs
    ) -> None:
        """Post a bunch of optional parameters grouped.

        :param parameter_grouping_post_optional_parameters: Parameter group.
        :type parameter_grouping_post_optional_parameters: ~azureparametergrouping.models.ParameterGroupingPostOptionalParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._post_optional_request(
            parameter_grouping_post_optional_parameters=parameter_grouping_post_optional_parameters, **kwargs
        )
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    post_optional.metadata = {"url": "/parameterGrouping/postOptional"}  # type: ignore

    def _post_multi_param_groups_request(
        self,
        first_parameter_group: Optional["_models.FirstParameterGroup"] = None,
        parameter_grouping_post_multi_param_groups_second_param_group: Optional[
            "_models.ParameterGroupingPostMultiParamGroupsSecondParamGroup"
        ] = None,
        **kwargs
    ) -> HttpRequest:

        _header_one = None
        _query_one = None
        _header_two = None
        _query_two = None
        if first_parameter_group is not None:
            _header_one = first_parameter_group.header_one
            _query_one = first_parameter_group.query_one
        if parameter_grouping_post_multi_param_groups_second_param_group is not None:
            _header_two = parameter_grouping_post_multi_param_groups_second_param_group.header_two
            _query_two = parameter_grouping_post_multi_param_groups_second_param_group.query_two
        accept = "application/json"

        # Construct URL
        url = self._post_multi_param_groups_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if _query_one is not None:
            query_parameters["query-one"] = self._serialize.query("query_one", _query_one, "int")
        if _query_two is not None:
            query_parameters["query-two"] = self._serialize.query("query_two", _query_two, "int")

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _header_one is not None:
            header_parameters["header-one"] = self._serialize.header("header_one", _header_one, "str")
        if _header_two is not None:
            header_parameters["header-two"] = self._serialize.header("header_two", _header_two, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.post(url, query_parameters, header_parameters)

    _post_multi_param_groups_request.metadata = {"url": "/parameterGrouping/postMultipleParameterGroups"}  # type: ignore

    @distributed_trace_async
    async def post_multi_param_groups(
        self,
        first_parameter_group: Optional["_models.FirstParameterGroup"] = None,
        parameter_grouping_post_multi_param_groups_second_param_group: Optional[
            "_models.ParameterGroupingPostMultiParamGroupsSecondParamGroup"
        ] = None,
        **kwargs
    ) -> None:
        """Post parameters from multiple different parameter groups.

        :param first_parameter_group: Parameter group.
        :type first_parameter_group: ~azureparametergrouping.models.FirstParameterGroup
        :param parameter_grouping_post_multi_param_groups_second_param_group: Parameter group.
        :type parameter_grouping_post_multi_param_groups_second_param_group: ~azureparametergrouping.models.ParameterGroupingPostMultiParamGroupsSecondParamGroup
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._post_multi_param_groups_request(
            first_parameter_group=first_parameter_group,
            parameter_grouping_post_multi_param_groups_second_param_group=parameter_grouping_post_multi_param_groups_second_param_group,
            **kwargs
        )
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    post_multi_param_groups.metadata = {"url": "/parameterGrouping/postMultipleParameterGroups"}  # type: ignore

    def _post_shared_parameter_group_object_request(
        self, first_parameter_group: Optional["_models.FirstParameterGroup"] = None, **kwargs
    ) -> HttpRequest:

        _header_one = None
        _query_one = None
        if first_parameter_group is not None:
            _header_one = first_parameter_group.header_one
            _query_one = first_parameter_group.query_one
        accept = "application/json"

        # Construct URL
        url = self._post_shared_parameter_group_object_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if _query_one is not None:
            query_parameters["query-one"] = self._serialize.query("query_one", _query_one, "int")

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _header_one is not None:
            header_parameters["header-one"] = self._serialize.header("header_one", _header_one, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.post(url, query_parameters, header_parameters)

    _post_shared_parameter_group_object_request.metadata = {"url": "/parameterGrouping/sharedParameterGroupObject"}  # type: ignore

    @distributed_trace_async
    async def post_shared_parameter_group_object(
        self, first_parameter_group: Optional["_models.FirstParameterGroup"] = None, **kwargs
    ) -> None:
        """Post parameters with a shared parameter group object.

        :param first_parameter_group: Parameter group.
        :type first_parameter_group: ~azureparametergrouping.models.FirstParameterGroup
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._post_shared_parameter_group_object_request(
            first_parameter_group=first_parameter_group, **kwargs
        )
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    post_shared_parameter_group_object.metadata = {"url": "/parameterGrouping/sharedParameterGroupObject"}  # type: ignore
