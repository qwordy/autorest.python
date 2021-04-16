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

from typing import Any, Optional, TYPE_CHECKING

from .._profiles import KnownProfiles, MultiApiClientMixin, ProfileDefinition
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration import MultiapiServiceClientConfiguration
from ._operations_mixin import MultiapiServiceClientOperationsMixin

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class MultiapiServiceClient(MultiapiServiceClientOperationsMixin, MultiApiClientMixin, _SDKClient):
    """Service client for multiapi client testing.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '3.0.0'
    _PROFILE_TAG = "multiapi.MultiapiServiceClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
            'begin_test_lro': '1.0.0',
            'begin_test_lro_and_paging': '1.0.0',
            'test_one': '2.0.0',
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        api_version: Optional[str] = None,
        base_url: Optional[str] = None,
        profile: KnownProfiles = KnownProfiles.default,
        **kwargs  # type: Any
    ) -> None:
        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = MultiapiServiceClientConfiguration(credential, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(MultiapiServiceClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 0.0.0: :mod:`v0.models<multiapi.v0.models>`
           * 1.0.0: :mod:`v1.models<multiapi.v1.models>`
           * 2.0.0: :mod:`v2.models<multiapi.v2.models>`
           * 3.0.0: :mod:`v3.models<multiapi.v3.models>`
        """
        if api_version == '0.0.0':
            from ..v0 import models
            return models
        elif api_version == '1.0.0':
            from ..v1 import models
            return models
        elif api_version == '2.0.0':
            from ..v2 import models
            return models
        elif api_version == '3.0.0':
            from ..v3 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def operation_group_one(self):
        """Instance depends on the API version:

           * 0.0.0: :class:`OperationGroupOneOperations<multiapi.v0.aio.operations.OperationGroupOneOperations>`
           * 1.0.0: :class:`OperationGroupOneOperations<multiapi.v1.aio.operations.OperationGroupOneOperations>`
           * 2.0.0: :class:`OperationGroupOneOperations<multiapi.v2.aio.operations.OperationGroupOneOperations>`
           * 3.0.0: :class:`OperationGroupOneOperations<multiapi.v3.aio.operations.OperationGroupOneOperations>`
        """
        api_version = self._get_api_version('operation_group_one')
        if api_version == '0.0.0':
            from ..v0.aio.operations import OperationGroupOneOperations as OperationClass
        elif api_version == '1.0.0':
            from ..v1.aio.operations import OperationGroupOneOperations as OperationClass
        elif api_version == '2.0.0':
            from ..v2.aio.operations import OperationGroupOneOperations as OperationClass
        elif api_version == '3.0.0':
            from ..v3.aio.operations import OperationGroupOneOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operation_group_one'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operation_group_two(self):
        """Instance depends on the API version:

           * 2.0.0: :class:`OperationGroupTwoOperations<multiapi.v2.aio.operations.OperationGroupTwoOperations>`
           * 3.0.0: :class:`OperationGroupTwoOperations<multiapi.v3.aio.operations.OperationGroupTwoOperations>`
        """
        api_version = self._get_api_version('operation_group_two')
        if api_version == '2.0.0':
            from ..v2.aio.operations import OperationGroupTwoOperations as OperationClass
        elif api_version == '3.0.0':
            from ..v3.aio.operations import OperationGroupTwoOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operation_group_two'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    async def close(self):
        await self._client.close()
    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
