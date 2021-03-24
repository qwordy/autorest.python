# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Optional

from azure.core.pipeline.transport._base import _format_url_section
from azure.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def prepare_parametergrouping_post_required(
    path: str, body: int, *, custom_header: Optional[str] = None, query: Optional[int] = 30, **kwargs: Any
) -> HttpRequest:
    """Post a bunch of required parameters grouped.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param path: Path parameter.
    :type path: str
    :param custom_header:
    :type custom_header: str
    :param query: Query parameter with default.
    :type query: int
    :param body:
    :type body: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/parameterGrouping/postRequired/{path}")
    path_format_arguments = {
        "path": _SERIALIZER.url("path", path, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if query is not None:
        query_parameters["query"] = _SERIALIZER.query("query", query, "int")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if custom_header is not None:
        header_parameters["customHeader"] = _SERIALIZER.header("custom_header", custom_header, "str")
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["json"] = body

    return HttpRequest(
        method="POST", url=url, params=query_parameters, headers=header_parameters, **body_content_kwargs
    )


def prepare_parametergrouping_post_optional(
    *, custom_header: Optional[str] = None, query: Optional[int] = 30, **kwargs: Any
) -> HttpRequest:
    """Post a bunch of optional parameters grouped.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param custom_header:
    :type custom_header: str
    :param query: Query parameter with default.
    :type query: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/parameterGrouping/postOptional")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if query is not None:
        query_parameters["query"] = _SERIALIZER.query("query", query, "int")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if custom_header is not None:
        header_parameters["customHeader"] = _SERIALIZER.header("custom_header", custom_header, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_parametergrouping_post_multi_param_groups(
    *,
    header_one: Optional[str] = None,
    query_one: Optional[int] = 30,
    header_two: Optional[str] = None,
    query_two: Optional[int] = 30,
    **kwargs: Any
) -> HttpRequest:
    """Post parameters from multiple different parameter groups.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param header_one:
    :type header_one: str
    :param query_one: Query parameter with default.
    :type query_one: int
    :param header_two:
    :type header_two: str
    :param query_two: Query parameter with default.
    :type query_two: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/parameterGrouping/postMultipleParameterGroups")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if query_one is not None:
        query_parameters["query-one"] = _SERIALIZER.query("query_one", query_one, "int")
    if query_two is not None:
        query_parameters["query-two"] = _SERIALIZER.query("query_two", query_two, "int")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if header_one is not None:
        header_parameters["header-one"] = _SERIALIZER.header("header_one", header_one, "str")
    if header_two is not None:
        header_parameters["header-two"] = _SERIALIZER.header("header_two", header_two, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_parametergrouping_post_shared_parameter_group_object(
    *, header_one: Optional[str] = None, query_one: Optional[int] = 30, **kwargs: Any
) -> HttpRequest:
    """Post parameters with a shared parameter group object.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param header_one:
    :type header_one: str
    :param query_one: Query parameter with default.
    :type query_one: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/parameterGrouping/sharedParameterGroupObject")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if query_one is not None:
        query_parameters["query-one"] = _SERIALIZER.query("query_one", query_one, "int")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if header_one is not None:
        header_parameters["header-one"] = _SERIALIZER.header("header_one", header_one, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )
