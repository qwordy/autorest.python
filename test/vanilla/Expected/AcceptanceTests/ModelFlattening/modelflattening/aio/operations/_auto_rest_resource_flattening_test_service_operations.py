# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
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


class AutoRestResourceFlatteningTestServiceOperationsMixin:
    def _put_array_request(self, body: Optional[List["_models.Resource"]] = None, **kwargs) -> HttpRequest:
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._put_array_request.metadata["url"])  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        if body is not None:
            body_content = self._serialize.body(body, "[Resource]")
        else:
            body_content = None
        body_content_kwargs["content"] = body_content
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    _put_array_request.metadata = {"url": "/model-flatten/array"}  # type: ignore

    @distributed_trace_async
    async def put_array(self, resource_array: Optional[List["_models.Resource"]] = None, **kwargs) -> None:
        """Put External Resource as an Array.

        :param resource_array: External Resource as an Array to put.
        :type resource_array: list[~modelflattening.models.Resource]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._put_array_request(body=resource_array, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_array.metadata = {"url": "/model-flatten/array"}  # type: ignore

    def _get_array_request(self, **kwargs) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._get_array_request.metadata["url"])  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_array_request.metadata = {"url": "/model-flatten/array"}  # type: ignore

    @distributed_trace_async
    async def get_array(self, **kwargs) -> List["_models.FlattenedProduct"]:
        """Get External Resource as an Array.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of FlattenedProduct, or the result of cls(response)
        :rtype: list[~modelflattening.models.FlattenedProduct]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[List["_models.FlattenedProduct"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_array_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("[FlattenedProduct]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_array.metadata = {"url": "/model-flatten/array"}  # type: ignore

    def _put_wrapped_array_request(
        self, body: Optional[List["_models.WrappedProduct"]] = None, **kwargs
    ) -> HttpRequest:
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._put_wrapped_array_request.metadata["url"])  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        if body is not None:
            body_content = self._serialize.body(body, "[WrappedProduct]")
        else:
            body_content = None
        body_content_kwargs["content"] = body_content
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    _put_wrapped_array_request.metadata = {"url": "/model-flatten/wrappedarray"}  # type: ignore

    @distributed_trace_async
    async def put_wrapped_array(
        self, resource_array: Optional[List["_models.WrappedProduct"]] = None, **kwargs
    ) -> None:
        """No need to have a route in Express server for this operation. Used to verify the type flattened
        is not removed if it's referenced in an array.

        :param resource_array: External Resource as an Array to put.
        :type resource_array: list[~modelflattening.models.WrappedProduct]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._put_wrapped_array_request(body=resource_array, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_wrapped_array.metadata = {"url": "/model-flatten/wrappedarray"}  # type: ignore

    def _get_wrapped_array_request(self, **kwargs) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._get_wrapped_array_request.metadata["url"])  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_wrapped_array_request.metadata = {"url": "/model-flatten/wrappedarray"}  # type: ignore

    @distributed_trace_async
    async def get_wrapped_array(self, **kwargs) -> List["_models.ProductWrapper"]:
        """No need to have a route in Express server for this operation. Used to verify the type flattened
        is not removed if it's referenced in an array.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of ProductWrapper, or the result of cls(response)
        :rtype: list[~modelflattening.models.ProductWrapper]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[List["_models.ProductWrapper"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_wrapped_array_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("[ProductWrapper]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_wrapped_array.metadata = {"url": "/model-flatten/wrappedarray"}  # type: ignore

    def _put_dictionary_request(
        self, body: Optional[Dict[str, "_models.FlattenedProduct"]] = None, **kwargs
    ) -> HttpRequest:
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._put_dictionary_request.metadata["url"])  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        if body is not None:
            body_content = self._serialize.body(body, "{FlattenedProduct}")
        else:
            body_content = None
        body_content_kwargs["content"] = body_content
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    _put_dictionary_request.metadata = {"url": "/model-flatten/dictionary"}  # type: ignore

    @distributed_trace_async
    async def put_dictionary(
        self, resource_dictionary: Optional[Dict[str, "_models.FlattenedProduct"]] = None, **kwargs
    ) -> None:
        """Put External Resource as a Dictionary.

        :param resource_dictionary: External Resource as a Dictionary to put.
        :type resource_dictionary: dict[str, ~modelflattening.models.FlattenedProduct]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._put_dictionary_request(body=resource_dictionary, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_dictionary.metadata = {"url": "/model-flatten/dictionary"}  # type: ignore

    def _get_dictionary_request(self, **kwargs) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._get_dictionary_request.metadata["url"])  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_dictionary_request.metadata = {"url": "/model-flatten/dictionary"}  # type: ignore

    @distributed_trace_async
    async def get_dictionary(self, **kwargs) -> Dict[str, "_models.FlattenedProduct"]:
        """Get External Resource as a Dictionary.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: dict mapping str to FlattenedProduct, or the result of cls(response)
        :rtype: dict[str, ~modelflattening.models.FlattenedProduct]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Dict[str, "_models.FlattenedProduct"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_dictionary_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("{FlattenedProduct}", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_dictionary.metadata = {"url": "/model-flatten/dictionary"}  # type: ignore

    def _put_resource_collection_request(
        self, body: Optional["_models.ResourceCollection"] = None, **kwargs
    ) -> HttpRequest:
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._put_resource_collection_request.metadata["url"])  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        if body is not None:
            body_content = self._serialize.body(body, "ResourceCollection")
        else:
            body_content = None
        body_content_kwargs["content"] = body_content
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    _put_resource_collection_request.metadata = {"url": "/model-flatten/resourcecollection"}  # type: ignore

    @distributed_trace_async
    async def put_resource_collection(
        self, resource_complex_object: Optional["_models.ResourceCollection"] = None, **kwargs
    ) -> None:
        """Put External Resource as a ResourceCollection.

        :param resource_complex_object: External Resource as a ResourceCollection to put.
        :type resource_complex_object: ~modelflattening.models.ResourceCollection
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._put_resource_collection_request(body=resource_complex_object, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_resource_collection.metadata = {"url": "/model-flatten/resourcecollection"}  # type: ignore

    def _get_resource_collection_request(self, **kwargs) -> HttpRequest:
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._get_resource_collection_request.metadata["url"])  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_resource_collection_request.metadata = {"url": "/model-flatten/resourcecollection"}  # type: ignore

    @distributed_trace_async
    async def get_resource_collection(self, **kwargs) -> "_models.ResourceCollection":
        """Get External Resource as a ResourceCollection.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ResourceCollection, or the result of cls(response)
        :rtype: ~modelflattening.models.ResourceCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ResourceCollection"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_resource_collection_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("ResourceCollection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_resource_collection.metadata = {"url": "/model-flatten/resourcecollection"}  # type: ignore

    def _put_simple_product_request(self, body: Optional["_models.SimpleProduct"] = None, **kwargs) -> HttpRequest:
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._put_simple_product_request.metadata["url"])  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        if body is not None:
            body_content = self._serialize.body(body, "SimpleProduct")
        else:
            body_content = None
        body_content_kwargs["content"] = body_content
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    _put_simple_product_request.metadata = {"url": "/model-flatten/customFlattening"}  # type: ignore

    @distributed_trace_async
    async def put_simple_product(
        self, simple_body_product: Optional["_models.SimpleProduct"] = None, **kwargs
    ) -> "_models.SimpleProduct":
        """Put Simple Product with client flattening true on the model.

        :param simple_body_product: Simple body product to put.
        :type simple_body_product: ~modelflattening.models.SimpleProduct
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SimpleProduct, or the result of cls(response)
        :rtype: ~modelflattening.models.SimpleProduct
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SimpleProduct"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._put_simple_product_request(body=simple_body_product, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SimpleProduct", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put_simple_product.metadata = {"url": "/model-flatten/customFlattening"}  # type: ignore

    def _post_flattened_simple_product_request(
        self, body: Optional["_models.SimpleProduct"] = None, **kwargs
    ) -> HttpRequest:
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._post_flattened_simple_product_request.metadata["url"])  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        if body is not None:
            body_content = self._serialize.body(body, "SimpleProduct")
        else:
            body_content = None
        body_content_kwargs["content"] = body_content
        return self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

    _post_flattened_simple_product_request.metadata = {"url": "/model-flatten/customFlattening"}  # type: ignore

    @distributed_trace_async
    async def post_flattened_simple_product(
        self,
        product_id: str,
        description: Optional[str] = None,
        max_product_display_name: Optional[str] = None,
        generic_value: Optional[str] = None,
        odata_value: Optional[str] = None,
        **kwargs
    ) -> "_models.SimpleProduct":
        """Put Flattened Simple Product with client flattening true on the parameter.

        :param product_id: Unique identifier representing a specific product for a given latitude &
         longitude. For example, uberX in San Francisco will have a different product_id than uberX in
         Los Angeles.
        :type product_id: str
        :param description: Description of product.
        :type description: str
        :param max_product_display_name: Display name of product.
        :type max_product_display_name: str
        :param generic_value: Generic URL value.
        :type generic_value: str
        :param odata_value: URL value.
        :type odata_value: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SimpleProduct, or the result of cls(response)
        :rtype: ~modelflattening.models.SimpleProduct
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SimpleProduct"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _simple_body_product = _models.SimpleProduct(
            product_id=product_id,
            description=description,
            max_product_display_name=max_product_display_name,
            generic_value=generic_value,
            odata_value=odata_value,
        )
        request = self._post_flattened_simple_product_request(body=_simple_body_product, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SimpleProduct", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    post_flattened_simple_product.metadata = {"url": "/model-flatten/customFlattening"}  # type: ignore

    def _put_simple_product_with_grouping_request(
        self, name: str, body: Optional["_models.SimpleProduct"] = None, **kwargs
    ) -> HttpRequest:
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._put_simple_product_with_grouping_request.metadata["url"])  # type: ignore
        path_format_arguments = {
            "name": self._serialize.url("name", name, "str"),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        if body is not None:
            body_content = self._serialize.body(body, "SimpleProduct")
        else:
            body_content = None
        body_content_kwargs["content"] = body_content
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    _put_simple_product_with_grouping_request.metadata = {"url": "/model-flatten/customFlattening/parametergrouping/{name}/"}  # type: ignore

    @distributed_trace_async
    async def put_simple_product_with_grouping(
        self, flatten_parameter_group: "_models.FlattenParameterGroup", **kwargs
    ) -> "_models.SimpleProduct":
        """Put Simple Product with client flattening true on the model.

        :param flatten_parameter_group: Parameter group.
        :type flatten_parameter_group: ~modelflattening.models.FlattenParameterGroup
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SimpleProduct, or the result of cls(response)
        :rtype: ~modelflattening.models.SimpleProduct
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SimpleProduct"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _name = None
        _simple_body_product = None
        _product_id = None
        _description = None
        _max_product_display_name = None
        _generic_value = None
        _odata_value = None
        if flatten_parameter_group is not None:
            _name = flatten_parameter_group.name
            _simple_body_product = flatten_parameter_group.simple_body_product
            _product_id = flatten_parameter_group.product_id
            _description = flatten_parameter_group.description
            _max_product_display_name = flatten_parameter_group.max_product_display_name
            _generic_value = flatten_parameter_group.generic_value
            _odata_value = flatten_parameter_group.odata_value
        _simple_body_product = _models.SimpleProduct(
            product_id=_product_id,
            description=_description,
            max_product_display_name=_max_product_display_name,
            generic_value=_generic_value,
            odata_value=_odata_value,
        )
        request = self._put_simple_product_with_grouping_request(name=_name, body=_simple_body_product, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SimpleProduct", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put_simple_product_with_grouping.metadata = {"url": "/model-flatten/customFlattening/parametergrouping/{name}/"}  # type: ignore
