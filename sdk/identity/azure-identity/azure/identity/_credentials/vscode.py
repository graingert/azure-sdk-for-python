# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import abc
import os
import sys
from typing import cast, TYPE_CHECKING

from .._exceptions import CredentialUnavailableError
from .._constants import AzureAuthorityHosts, AZURE_VSCODE_CLIENT_ID, EnvironmentVariables
from .._internal import normalize_authority, validate_tenant_id
from .._internal.aad_client import AadClient
from .._internal.get_token_mixin import GetTokenMixin

if sys.platform.startswith("win"):
    from .._internal.win_vscode_adapter import get_refresh_token, get_user_settings
elif sys.platform.startswith("darwin"):
    from .._internal.macos_vscode_adapter import get_refresh_token, get_user_settings
else:
    from .._internal.linux_vscode_adapter import get_refresh_token, get_user_settings

if TYPE_CHECKING:
    # pylint:disable=unused-import,ungrouped-imports
    from typing import Any, Dict, Optional
    from azure.core.credentials import AccessToken
    from .._internal.aad_client import AadClientBase

try:
    ABC = abc.ABC
except AttributeError:  # Python 2.7, abc exists, but not ABC
    ABC = abc.ABCMeta("ABC", (object,), {"__slots__": ()})  # type: ignore


class _VSCodeCredentialBase(ABC):
    def __init__(self, **kwargs):
        # type: (**Any) -> None
        super(_VSCodeCredentialBase, self).__init__()

        user_settings = get_user_settings()
        self._cloud = user_settings.get("azure.cloud", "AzureCloud")
        self._refresh_token = None
        self._unavailable_reason = ""

        self._client = kwargs.get("_client")
        if not self._client:
            self._initialize(user_settings, **kwargs)
        if not (self._client or self._unavailable_reason):
            self._unavailable_reason = "Initialization failed"

    @abc.abstractmethod
    def _get_client(self, **kwargs):
        # type: (**Any) -> AadClientBase
        pass

    def _get_refresh_token(self):
        # type: () -> str
        if not self._refresh_token:
            self._refresh_token = get_refresh_token(self._cloud)
            if not self._refresh_token:
                raise CredentialUnavailableError(message="Failed to get Azure user details from Visual Studio Code.")
        return self._refresh_token

    def _initialize(self, vscode_user_settings, **kwargs):
        # type: (Dict, **Any) -> None
        """Build a client from kwargs merged with VS Code user settings.

        The first stable version of this credential defaulted to Public Cloud and the "organizations"
        tenant when it failed to read VS Code user settings. That behavior is preserved here.
        """

        # Precedence for authority:
        #  1) VisualStudioCodeCredential(authority=...)
        #  2) $AZURE_AUTHORITY_HOST
        #  3) authority matching VS Code's "azure.cloud" setting
        #  4) default: Public Cloud
        authority = kwargs.pop("authority", None) or os.environ.get(EnvironmentVariables.AZURE_AUTHORITY_HOST)
        if not authority:
            # the application didn't specify an authority, so we figure it out from VS Code settings
            if self._cloud == "AzureCloud":
                authority = AzureAuthorityHosts.AZURE_PUBLIC_CLOUD
            elif self._cloud == "AzureChinaCloud":
                authority = AzureAuthorityHosts.AZURE_CHINA
            elif self._cloud == "AzureGermanCloud":
                authority = AzureAuthorityHosts.AZURE_GERMANY
            elif self._cloud == "AzureUSGovernment":
                authority = AzureAuthorityHosts.AZURE_GOVERNMENT
            else:
                # If the value is anything else ("AzureCustomCloud" is the only other known value),
                # we need the user to provide the authority because VS Code has no setting for it and
                # we can't guess confidently.
                self._unavailable_reason = (
                    'VS Code is configured to use a custom cloud. Set keyword argument "authority"'
                    + ' with the Azure Active Directory endpoint for cloud "{}"'.format(self._cloud)
                )
                return

        # Precedence for tenant ID:
        #  1) VisualStudioCodeCredential(tenant_id=...)
        #  2) "azure.tenant" in VS Code user settings
        #  3) default: organizations
        tenant_id = kwargs.pop("tenant_id", None) or vscode_user_settings.get("azure.tenant", "organizations")
        validate_tenant_id(tenant_id)
        if tenant_id.lower() == "adfs":
            self._unavailable_reason = "VisualStudioCodeCredential authentication unavailable. ADFS is not supported."
            return

        self._client = self._get_client(
            authority=normalize_authority(authority), client_id=AZURE_VSCODE_CLIENT_ID, tenant_id=tenant_id, **kwargs
        )


class VisualStudioCodeCredential(_VSCodeCredentialBase, GetTokenMixin):
    """Authenticates as the Azure user signed in to Visual Studio Code.

    :keyword str authority: authority of an Azure Active Directory endpoint, for example "login.microsoftonline.com".
        This argument is required for a custom cloud and usually unnecessary otherwise. Defaults to the authority
        matching the "Azure: Cloud" setting in VS Code's user settings or, when that setting has no value, the
        authority for Azure Public Cloud.
    :keyword str tenant_id: ID of the tenant the credential should authenticate in. Defaults to the "Azure: Tenant"
        setting in VS Code's user settings or, when that setting has no value, the "organizations" tenant, which
        supports only Azure Active Directory work or school accounts.
    :keyword bool allow_multitenant_authentication: when True, enables the credential to acquire tokens from any tenant
        the user is registered in. When False, which is the default, the credential will acquire tokens only from the
        user's home tenant or the tenant configured by **tenant_id** or VS Code's user settings.
    """

    def get_token(self, *scopes, **kwargs):
        # type: (*str, **Any) -> AccessToken
        """Request an access token for `scopes` as the user currently signed in to Visual Studio Code.

        This method is called automatically by Azure SDK clients.

        :param str scopes: desired scopes for the access token. This method requires at least one scope.
        :rtype: :class:`azure.core.credentials.AccessToken`
        :raises ~azure.identity.CredentialUnavailableError: the credential cannot retrieve user details from Visual
          Studio Code
        """
        if self._unavailable_reason:
            raise CredentialUnavailableError(message=self._unavailable_reason)
        return super(VisualStudioCodeCredential, self).get_token(*scopes, **kwargs)

    def _acquire_token_silently(self, *scopes, **kwargs):
        # type: (*str, **Any) -> Optional[AccessToken]
        self._client = cast(AadClient, self._client)
        return self._client.get_cached_access_token(scopes, **kwargs)

    def _request_token(self, *scopes, **kwargs):
        # type: (*str, **Any) -> AccessToken
        refresh_token = self._get_refresh_token()
        self._client = cast(AadClient, self._client)
        return self._client.obtain_token_by_refresh_token(scopes, refresh_token, **kwargs)

    def _get_client(self, **kwargs):
        # type: (**Any) -> AadClient
        return AadClient(**kwargs)
