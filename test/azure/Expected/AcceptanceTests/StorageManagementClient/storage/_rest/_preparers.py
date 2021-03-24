# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.pipeline.transport._base import _format_url_section
from azure.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional, Union

_SERIALIZER = Serializer()


def prepare_storageaccounts_check_name_availability(
    subscription_id,  # type: str
    account_name,  # type: "_models.StorageAccountCheckNameAvailabilityParameters"
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Checks that account name is valid and is not in use.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param account_name: The name of the storage account within the specified resource group.
     Storage account names must be between 3 and 24 characters in length and use numbers and lower-
     case letters only.
    :type account_name: ~storage.models.StorageAccountCheckNameAvailabilityParameters
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    api_version = "2015-05-01-preview"
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Storage/checkNameAvailability"
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["json"] = account_name

    return HttpRequest(
        method="POST", url=url, params=query_parameters, headers=header_parameters, **body_content_kwargs
    )


def prepare_storageaccounts_create_initial(
    resource_group_name,  # type: str
    account_name,  # type: str
    subscription_id,  # type: str
    parameters,  # type: "_models.StorageAccountCreateParameters"
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Asynchronously creates a new storage account with the specified parameters. Existing accounts
    cannot be updated with this API and should instead use the Update Storage Account API. If an
    account is already created and subsequent PUT request is issued with exact same set of
    properties, then HTTP 200 would be returned.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param resource_group_name: The name of the resource group within the user’s subscription.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group.
     Storage account names must be between 3 and 24 characters in length and use numbers and lower-
     case letters only.
    :type account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The parameters to provide for the created account.
    :type parameters: ~storage.models.StorageAccountCreateParameters
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    api_version = "2015-05-01-preview"
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["json"] = parameters

    return HttpRequest(method="PUT", url=url, params=query_parameters, headers=header_parameters, **body_content_kwargs)


def prepare_storageaccounts_delete(
    resource_group_name,  # type: str
    account_name,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Deletes a storage account in Microsoft Azure.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param resource_group_name: The name of the resource group within the user’s subscription.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group.
     Storage account names must be between 3 and 24 characters in length and use numbers and lower-
     case letters only.
    :type account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    api_version = "2015-05-01-preview"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
    )


def prepare_storageaccounts_get_properties(
    resource_group_name,  # type: str
    account_name,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Returns the properties for the specified storage account including but not limited to name,
    account type, location, and account status. The ListKeys operation should be used to retrieve
    storage keys.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param resource_group_name: The name of the resource group within the user’s subscription.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group.
     Storage account names must be between 3 and 24 characters in length and use numbers and lower-
     case letters only.
    :type account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    api_version = "2015-05-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_storageaccounts_update(
    resource_group_name,  # type: str
    account_name,  # type: str
    subscription_id,  # type: str
    parameters,  # type: "_models.StorageAccountUpdateParameters"
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Updates the account type or tags for a storage account. It can also be used to add a custom
    domain (note that custom domains cannot be added via the Create operation). Only one custom
    domain is supported per storage account. This API can only be used to update one of tags,
    accountType, or customDomain per call. To update multiple of these properties, call the API
    multiple times with one change per call. This call does not change the storage keys for the
    account. If you want to change storage account keys, use the RegenerateKey operation. The
    location and name of the storage account cannot be changed after creation.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param resource_group_name: The name of the resource group within the user’s subscription.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group.
     Storage account names must be between 3 and 24 characters in length and use numbers and lower-
     case letters only.
    :type account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The parameters to update on the account. Note that only one property can be
     changed at a time using this API.
    :type parameters: ~storage.models.StorageAccountUpdateParameters
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    api_version = "2015-05-01-preview"
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["json"] = parameters

    return HttpRequest(
        method="PATCH", url=url, params=query_parameters, headers=header_parameters, **body_content_kwargs
    )


def prepare_storageaccounts_list_keys(
    resource_group_name,  # type: str
    account_name,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Lists the access keys for the specified storage account.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param resource_group_name: The name of the resource group within the user’s subscription.
    :type resource_group_name: str
    :param account_name: The name of the storage account.
    :type account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    api_version = "2015-05-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/listKeys",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_storageaccounts_list(
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Lists all the storage accounts available under the subscription. Note that storage keys are not
    returned; use the ListKeys operation for this.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    api_version = "2015-05-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Storage/storageAccounts")
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_storageaccounts_list_by_resource_group(
    resource_group_name,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Lists all the storage accounts available under the given resource group. Note that storage keys
    are not returned; use the ListKeys operation for this.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param resource_group_name: The name of the resource group within the user’s subscription.
    :type resource_group_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    api_version = "2015-05-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_storageaccounts_regenerate_key(
    resource_group_name,  # type: str
    account_name,  # type: str
    subscription_id,  # type: str
    regenerate_key,  # type: "_models.StorageAccountRegenerateKeyParameters"
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Regenerates the access keys for the specified storage account.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param resource_group_name: The name of the resource group within the user’s subscription.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group.
     Storage account names must be between 3 and 24 characters in length and use numbers and lower-
     case letters only.
    :type account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param regenerate_key: Specifies name of the key which should be regenerated.
    :type regenerate_key: ~storage.models.StorageAccountRegenerateKeyParameters
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    api_version = "2015-05-01-preview"
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/regenerateKey",
    )
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["json"] = regenerate_key

    return HttpRequest(
        method="POST", url=url, params=query_parameters, headers=header_parameters, **body_content_kwargs
    )


def prepare_usage_list(
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Gets the current usage count and the limit for the resources under the subscription.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    api_version = "2015-05-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Storage/usages")
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )
