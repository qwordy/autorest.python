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
from azure.core import HttpRequestError
from msrest.polling.async_poller import async_poller, AsyncNoPolling
from msrestazure.polling.async_arm_polling import AsyncARMPolling

from ... import models


class StorageAccountsOperations:
    """StorageAccountsOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Client Api Version. Constant value: "2015-05-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2015-05-01-preview"

        self._config = config

    async def check_name_availability(self, account_name, *, cls=None, **kwargs):
        """Checks that account name is valid and is not in use.

        :param account_name: The name of the storage account within the
         specified resource group. Storage account names must be between 3 and
         24 characters in length and use numbers and lower-case letters only.
        :type account_name:
         ~storage.models.StorageAccountCheckNameAvailabilityParameters
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: CheckNameAvailabilityResult or the result of cls(response)
        :rtype: ~storage.models.CheckNameAvailabilityResult
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.check_name_availability.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(account_name, 'StorageAccountCheckNameAvailabilityParameters')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            error = self._map_error(status_code=response.status_code, response=response, error_map=kwargs.get('error_map'))
            exp = HttpRequestError(response=response)
            raise exp

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('CheckNameAvailabilityResult', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    check_name_availability.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Storage/checkNameAvailability'}


    async def _create_initial(
            self, resource_group_name, account_name, parameters, *, cls=None, **kwargs):
        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'StorageAccountCreateParameters')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            error = self._map_error(status_code=response.status_code, response=response, error_map=kwargs.get('error_map'))
            exp = HttpRequestError(response=response)
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('StorageAccount', response)

        return deserialized

    async def create(
            self, resource_group_name, account_name, parameters, *, cls=None, polling=True, **kwargs):
        """Asynchronously creates a new storage account with the specified
        parameters. Existing accounts cannot be updated with this API and
        should instead use the Update Storage Account API. If an account is
        already created and subsequent PUT request is issued with exact same
        set of properties, then HTTP 200 would be returned. .

        :param resource_group_name: The name of the resource group within the
         user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the
         specified resource group. Storage account names must be between 3 and
         24 characters in length and use numbers and lower-case letters only.
        :type account_name: str
        :param parameters: The parameters to provide for the created account.
        :type parameters: ~storage.models.StorageAccountCreateParameters
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of StorageAccount
        :rtype: ~~storage.models.StorageAccount
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        raw_result = await self._create_initial(
            resource_group_name=resource_group_name,
            account_name=account_name,
            parameters=parameters,
            **kwargs
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('StorageAccount', response)

            return deserialized

        lro_delay = kwargs.get(
            'long_running_operation_timeout',
            self._config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self, raw_result, get_long_running_output, polling_method)
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}'}

    async def delete(self, resource_group_name, account_name, *, cls=None, **kwargs):
        """Deletes a storage account in Microsoft Azure.

        :param resource_group_name: The name of the resource group within the
         user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the
         specified resource group. Storage account names must be between 3 and
         24 characters in length and use numbers and lower-case letters only.
        :type account_name: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            error = self._map_error(status_code=response.status_code, response=response, error_map=kwargs.get('error_map'))
            exp = HttpRequestError(response=response)
            raise exp

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}'}

    async def get_properties(self, resource_group_name, account_name, *, cls=None, **kwargs):
        """Returns the properties for the specified storage account including but
        not limited to name, account type, location, and account status. The
        ListKeys operation should be used to retrieve storage keys.

        :param resource_group_name: The name of the resource group within the
         user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the
         specified resource group. Storage account names must be between 3 and
         24 characters in length and use numbers and lower-case letters only.
        :type account_name: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: StorageAccount or the result of cls(response)
        :rtype: ~storage.models.StorageAccount
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.get_properties.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            error = self._map_error(status_code=response.status_code, response=response, error_map=kwargs.get('error_map'))
            exp = HttpRequestError(response=response)
            raise exp

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('StorageAccount', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_properties.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}'}

    async def update(self, resource_group_name, account_name, parameters, *, cls=None, **kwargs):
        """Updates the account type or tags for a storage account. It can also be
        used to add a custom domain (note that custom domains cannot be added
        via the Create operation). Only one custom domain is supported per
        storage account. This API can only be used to update one of tags,
        accountType, or customDomain per call. To update multiple of these
        properties, call the API multiple times with one change per call. This
        call does not change the storage keys for the account. If you want to
        change storage account keys, use the RegenerateKey operation. The
        location and name of the storage account cannot be changed after
        creation.

        :param resource_group_name: The name of the resource group within the
         user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the
         specified resource group. Storage account names must be between 3 and
         24 characters in length and use numbers and lower-case letters only.
        :type account_name: str
        :param parameters: The parameters to update on the account. Note that
         only one property can be changed at a time using this API.
        :type parameters: ~storage.models.StorageAccountUpdateParameters
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: StorageAccount or the result of cls(response)
        :rtype: ~storage.models.StorageAccount
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'StorageAccountUpdateParameters')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            error = self._map_error(status_code=response.status_code, response=response, error_map=kwargs.get('error_map'))
            exp = HttpRequestError(response=response)
            raise exp

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('StorageAccount', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}'}

    async def list_keys(self, resource_group_name, account_name, *, cls=None, **kwargs):
        """Lists the access keys for the specified storage account.

        :param resource_group_name: The name of the resource group within the
         user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account.
        :type account_name: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: StorageAccountKeys or the result of cls(response)
        :rtype: ~storage.models.StorageAccountKeys
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.list_keys.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            error = self._map_error(status_code=response.status_code, response=response, error_map=kwargs.get('error_map'))
            exp = HttpRequestError(response=response)
            raise exp

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('StorageAccountKeys', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    list_keys.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/listKeys'}

    def list(
            self, *, cls=None, **kwargs):
        """Lists all the storage accounts available under the subscription. Note
        that storage keys are not returned; use the ListKeys operation for
        this.

        :return: An iterator like instance of StorageAccount
        :rtype:
         ~storage.models.StorageAccountPaged[~storage.models.StorageAccount]
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self._config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if self._config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._map_error(status_code=response.status_code, response=response, error_map=kwargs.get('error_map'))
                exp = HttpRequestError(response=response)
                raise exp

            return response

        async def internal_paging_async(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._map_error(status_code=response.status_code, response=response, error_map=kwargs.get('error_map'))
                exp = HttpRequestError(response=response)
                raise exp

            return response

        # Deserialize response
        header_dict = None
        deserialized = models.StorageAccountPaged(
            internal_paging, self._deserialize.dependencies, header_dict, async_command=internal_paging_async)

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Storage/storageAccounts'}

    def list_by_resource_group(
            self, resource_group_name, *, cls=None, **kwargs):
        """Lists all the storage accounts available under the given resource
        group. Note that storage keys are not returned; use the ListKeys
        operation for this.

        :param resource_group_name: The name of the resource group within the
         user’s subscription.
        :type resource_group_name: str
        :return: An iterator like instance of StorageAccount
        :rtype:
         ~storage.models.StorageAccountPaged[~storage.models.StorageAccount]
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_resource_group.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self._config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if self._config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._map_error(status_code=response.status_code, response=response, error_map=kwargs.get('error_map'))
                exp = HttpRequestError(response=response)
                raise exp

            return response

        async def internal_paging_async(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._map_error(status_code=response.status_code, response=response, error_map=kwargs.get('error_map'))
                exp = HttpRequestError(response=response)
                raise exp

            return response

        # Deserialize response
        header_dict = None
        deserialized = models.StorageAccountPaged(
            internal_paging, self._deserialize.dependencies, header_dict, async_command=internal_paging_async)

        return deserialized
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts'}

    async def regenerate_key(self, resource_group_name, account_name, key_name=None, *, cls=None, **kwargs):
        """Regenerates the access keys for the specified storage account.

        :param resource_group_name: The name of the resource group within the
         user’s subscription.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the
         specified resource group. Storage account names must be between 3 and
         24 characters in length and use numbers and lower-case letters only.
        :type account_name: str
        :param key_name: Possible values include: 'key1', 'key2'
        :type key_name: str or ~storage.models.KeyName
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: StorageAccountKeys or the result of cls(response)
        :rtype: ~storage.models.StorageAccountKeys
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        regenerate_key1 = models.StorageAccountRegenerateKeyParameters(key_name=key_name)

        # Construct URL
        url = self.regenerate_key.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(regenerate_key1, 'StorageAccountRegenerateKeyParameters')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            error = self._map_error(status_code=response.status_code, response=response, error_map=kwargs.get('error_map'))
            exp = HttpRequestError(response=response)
            raise exp

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('StorageAccountKeys', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    regenerate_key.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/regenerateKey'}