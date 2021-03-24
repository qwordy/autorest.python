# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, IO, Optional, Union

_SERIALIZER = Serializer()


def prepare_analyze_body(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Analyze body, that could be different media types.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param json: Input parameter.
    :type json: IO
    :param content: Input parameter.
    :type content: ~mediatypes.models.SourcePath
    :param content_type: Upload file type.
    :type content_type: str or ~mediatypes.models.ContentType
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    content_type = kwargs.pop("content_type", None)  # type: Optional[Union[str, "_models.ContentType"]]
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/mediatypes/analyze")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, **kwargs)


def prepare_content_type_with_encoding(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Pass in contentType 'text/plain; encoding=UTF-8' to pass test. Value for input does not matter.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param content: Input parameter.
    :type content: str
    :param content_type: Upload file type.
    :type content_type: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    content_type = kwargs.pop("content_type", "text/plain")  # type: Optional[str]
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/mediatypes/contentTypeWithEncoding")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, **kwargs)
