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
from msrest import Serializer, Deserializer
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

def inspect_args_for_api_version(func):
    # this maps (api_version, function_name) to a list of parameters that are not allowed
    # for that function call with that api_version
    unallowed_params_mapping = {
        ('1.0.0', 'test_different_calls'): ['greeting_in_chinese', 'greeting_in_french'],
        ('2.0.0', 'test_different_calls'): ['greeting_in_french'],
    }

    param_to_api_version_added = {
        'greeting_in_chinese': '2.0.0',
        'greeting_in_french': '3.0.0',
    }
    def wrapper(self, *args, **kwargs):
        func_name = func.__name__
        api_version = self._get_api_version(func_name)
        unallowed_parameters = [
            kwarg for kwarg in kwargs.keys()
            if kwarg in unallowed_params_mapping.get((api_version, func_name), [])
        ]
        if unallowed_parameters:
            param_to_api_version_error_strings = [
                "'{}' was added in api version '{}'".format(param, param_to_api_version_added[param])
                for param in unallowed_parameters
            ]
            raise ValueError(
                "Passed in parameter(s) '{}' not valid with api version '{}': {}".format(
                    "', '".join(unallowed_parameters),
                    api_version,
                    ", ".join(param_to_api_version_error_strings)
                )
            )
        return func(self, *args, **kwargs)
    return wrapper

class MultiapiServiceClientOperationsMixin(object):

    async def begin_test_lro(
        self,
        product: Optional["models.Product"] = None,
        **kwargs
    ) -> AsyncLROPoller["models.Product"]:
        """Put in whatever shape of Product you want, will return a Product with id equal to 100.

        :param product: Product to put.
        :type product: ~multiapicredentialdefaultpolicy.v1.models.Product
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either Product or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~multiapicredentialdefaultpolicy.v1.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_test_lro')
        if api_version == '1.0.0':
            from ..v1.aio.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_test_lro'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.begin_test_lro(product, **kwargs)

    def begin_test_lro_and_paging(
        self,
        client_request_id: Optional[str] = None,
        test_lro_and_paging_options: Optional["models.TestLroAndPagingOptions"] = None,
        **kwargs
    ) -> AsyncLROPoller[AsyncItemPaged["models.PagingResult"]]:
        """A long-running paging operation that includes a nextLink that has 10 pages.

        :param client_request_id:
        :type client_request_id: str
        :param test_lro_and_paging_options: Parameter group.
        :type test_lro_and_paging_options: ~multiapicredentialdefaultpolicy.v1.models.TestLroAndPagingOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns an iterator like instance of either PagingResult or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.core.async_paging.AsyncItemPaged[~multiapicredentialdefaultpolicy.v1.models.PagingResult]]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_test_lro_and_paging')
        if api_version == '1.0.0':
            from ..v1.aio.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_test_lro_and_paging'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.begin_test_lro_and_paging(client_request_id, test_lro_and_paging_options, **kwargs)

    @inspect_args_for_api_version
    async def test_different_calls(
        self,
        greeting_in_english: str,
        greeting_in_chinese: Optional[str] = None,
        greeting_in_french: Optional[str] = None,
        **kwargs
    ) -> None:
        """Has added parameters across the API versions.

        :param greeting_in_english: pass in 'hello' to pass test.
        :type greeting_in_english: str
        :param greeting_in_chinese: pass in 'nihao' to pass test.
        :type greeting_in_chinese: str
        :param greeting_in_french: pass in 'bonjour' to pass test.
        :type greeting_in_french: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        **New in API version 2.0.0**
            The parameter *greeting_in_chinese*
        **New in API version 3.0.0**
            The parameter *greeting_in_french*
        """
        api_version = self._get_api_version('test_different_calls')
        if api_version == '1.0.0':
            from ..v1.aio.operations import MultiapiServiceClientOperationsMixin as OperationClass
        elif api_version == '2.0.0':
            from ..v2.aio.operations import MultiapiServiceClientOperationsMixin as OperationClass
        elif api_version == '3.0.0':
            from ..v3.aio.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'test_different_calls'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))

        if api_version in ['1.0.0']:
            return await mixin_instance.test_different_calls(greeting_in_english, **kwargs)
        elif api_version in ['2.0.0']:
            return await mixin_instance.test_different_calls(greeting_in_english, greeting_in_chinese, **kwargs)
        return await mixin_instance.test_different_calls(greeting_in_english, greeting_in_chinese, greeting_in_french, **kwargs)

    async def test_one(
        self,
        id: int,
        message: Optional[str] = None,
        **kwargs
    ) -> "models.ModelTwo":
        """TestOne should be in an SecondVersionOperationsMixin. Returns ModelTwo.

        :param id: An int parameter.
        :type id: int
        :param message: An optional string parameter.
        :type message: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ModelTwo, or the result of cls(response)
        :rtype: ~multiapicredentialdefaultpolicy.v2.models.ModelTwo
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('test_one')
        if api_version == '1.0.0':
            from ..v1.aio.operations import MultiapiServiceClientOperationsMixin as OperationClass
        elif api_version == '2.0.0':
            from ..v2.aio.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'test_one'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.test_one(id, message, **kwargs)

    def test_paging(
        self,
        **kwargs
    ) -> AsyncItemPaged["models.PagingResult"]:
        """Returns ModelThree with optionalProperty 'paged'.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PagingResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~multiapicredentialdefaultpolicy.v3.models.PagingResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('test_paging')
        if api_version == '3.0.0':
            from ..v3.aio.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'test_paging'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.test_paging(**kwargs)
