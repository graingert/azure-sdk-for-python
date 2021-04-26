# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Dict, List, Optional

from azure.core.pipeline.transport._base import _format_url_section
from azure.farmbeats.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def build_list_by_farmer_id_request(
    farmer_id: str,
    *,
    resource_ids: Optional[List[str]] = None,
    resource_types: Optional[List[str]] = None,
    ids: Optional[List[str]] = None,
    names: Optional[List[str]] = None,
    property_filters: Optional[List[str]] = None,
    statuses: Optional[List[str]] = None,
    min_created_date_time: Optional[datetime.datetime] = None,
    max_created_date_time: Optional[datetime.datetime] = None,
    min_last_modified_date_time: Optional[datetime.datetime] = None,
    max_last_modified_date_time: Optional[datetime.datetime] = None,
    max_page_size: Optional[int] = 50,
    skip_token: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    """Returns a paginated list of attachment resources under a particular farmer.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :param farmer_id: Id of the associated farmer.
    :type farmer_id: str
    :keyword resource_ids: Resource Ids of the resource.
    :paramtype resource_ids: list[str]
    :keyword resource_types: Resource Types of the resource.
    :paramtype resource_types: list[str]
    :keyword ids: Ids of the resource.
    :paramtype ids: list[str]
    :keyword names: Names of the resource.
    :paramtype names: list[str]
    :keyword property_filters: Filters on key-value pairs within the Properties object.
     eg. "{testkey} eq {testvalue}".
    :paramtype property_filters: list[str]
    :keyword statuses: Statuses of the resource.
    :paramtype statuses: list[str]
    :keyword min_created_date_time: Minimum creation date of resource (inclusive).
    :paramtype min_created_date_time: ~datetime.datetime
    :keyword max_created_date_time: Maximum creation date of resource (inclusive).
    :paramtype max_created_date_time: ~datetime.datetime
    :keyword min_last_modified_date_time: Minimum last modified date of resource (inclusive).
    :paramtype min_last_modified_date_time: ~datetime.datetime
    :keyword max_last_modified_date_time: Maximum last modified date of resource (inclusive).
    :paramtype max_last_modified_date_time: ~datetime.datetime
    :keyword max_page_size: Maximum number of items needed (inclusive).
     Minimum = 10, Maximum = 1000, Default value = 50.
    :paramtype max_page_size: int
    :keyword skip_token: Skip token for getting next set of results.
    :paramtype skip_token: str
    :return: Returns an :class:`~azure.farmbeats.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.farmbeats.core.rest.HttpRequest
    """
    api_version = "2021-03-31-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/farmers/{farmerId}/attachments')
    path_format_arguments = {
        'farmerId': _SERIALIZER.url("farmer_id", farmer_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if resource_ids is not None:
        query_parameters['resourceIds'] = [_SERIALIZER.query("resource_ids", q, 'str') if q is not None else '' for q in resource_ids]
    if resource_types is not None:
        query_parameters['resourceTypes'] = [_SERIALIZER.query("resource_types", q, 'str') if q is not None else '' for q in resource_types]
    if ids is not None:
        query_parameters['ids'] = [_SERIALIZER.query("ids", q, 'str') if q is not None else '' for q in ids]
    if names is not None:
        query_parameters['names'] = [_SERIALIZER.query("names", q, 'str') if q is not None else '' for q in names]
    if property_filters is not None:
        query_parameters['propertyFilters'] = [_SERIALIZER.query("property_filters", q, 'str') if q is not None else '' for q in property_filters]
    if statuses is not None:
        query_parameters['statuses'] = [_SERIALIZER.query("statuses", q, 'str') if q is not None else '' for q in statuses]
    if min_created_date_time is not None:
        query_parameters['minCreatedDateTime'] = _SERIALIZER.query("min_created_date_time", min_created_date_time, 'iso-8601')
    if max_created_date_time is not None:
        query_parameters['maxCreatedDateTime'] = _SERIALIZER.query("max_created_date_time", max_created_date_time, 'iso-8601')
    if min_last_modified_date_time is not None:
        query_parameters['minLastModifiedDateTime'] = _SERIALIZER.query("min_last_modified_date_time", min_last_modified_date_time, 'iso-8601')
    if max_last_modified_date_time is not None:
        query_parameters['maxLastModifiedDateTime'] = _SERIALIZER.query("max_last_modified_date_time", max_last_modified_date_time, 'iso-8601')
    if max_page_size is not None:
        query_parameters['$maxPageSize'] = _SERIALIZER.query("max_page_size", max_page_size, 'int', maximum=1000, minimum=10)
    if skip_token is not None:
        query_parameters['$skipToken'] = _SERIALIZER.query("skip_token", skip_token, 'str')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_request(
    farmer_id: str,
    attachment_id: str,
    **kwargs: Any
) -> HttpRequest:
    """Gets a specified attachment resource under a particular farmer.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :param farmer_id: Id of the associted farmer.
    :type farmer_id: str
    :param attachment_id: Id of the attachment.
    :type attachment_id: str
    :return: Returns an :class:`~azure.farmbeats.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.farmbeats.core.rest.HttpRequest
    """
    api_version = "2021-03-31-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/farmers/{farmerId}/attachments/{attachmentId}')
    path_format_arguments = {
        'farmerId': _SERIALIZER.url("farmer_id", farmer_id, 'str'),
        'attachmentId': _SERIALIZER.url("attachment_id", attachment_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_create_or_update_request(
    farmer_id: str,
    attachment_id: str,
    *,
    files: Optional[Dict[str, Any]] = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    """Creates or updates an attachment resource under a particular farmer.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :param farmer_id: Id of the associated farmer resource.
    :type farmer_id: str
    :param attachment_id: Id of the attachment resource.
    :type attachment_id: str
    :keyword files: Multipart input for files. See the template in our example to find the input
     shape.
    :paramtype files: dict[str, Any]
    :keyword content: Multipart input for files. See the template in our example to find the input
     shape.
    :paramtype content: Any
    :return: Returns an :class:`~azure.farmbeats.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.farmbeats.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # multipart input template you can fill out and use as your `files` input.
            files = {
                "created_date_time": "str (optional). Date when resource was created.",
                "description": "str (optional). Textual description of resource.",
                "e_tag": "str (optional). The ETag value to implement optimistic concurrency.",
                "farmer_id1": "str (optional). Farmer id for this attachment.",
                "file": "IO (optional). File to be uploaded.",
                "id": "str (optional). Unique id.",
                "modified_date_time": "str (optional). Date when resource was last modified.",
                "name": "str (optional). Name to identify resource.",
                "original_file_name": "str (optional). Original File Name for this attachment.",
                "resource_id": "str (optional). Associated Resource id for this attachment.",
                "resource_type": "str (optional). Associated Resource type for this attachment\ni.e. Farmer, Farm, Field, SeasonalField, Boundary, FarmOperationApplicationData, HarvestData, TillageData, PlantingData.",
                "status": "str (optional). Status of the resource."
            }
    """
    content_type = kwargs.pop("content_type", None)
    api_version = "2021-03-31-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/farmers/{farmerId}/attachments/{attachmentId}')
    path_format_arguments = {
        'farmerId': _SERIALIZER.url("farmer_id", farmer_id, 'str'),
        'attachmentId': _SERIALIZER.url("attachment_id", attachment_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    return HttpRequest(
        method="PATCH",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        content=content,
        files=files,
        **kwargs
    )


def build_delete_request(
    farmer_id: str,
    attachment_id: str,
    **kwargs: Any
) -> HttpRequest:
    """Deletes a specified attachment resource under a particular farmer.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :param farmer_id: Id of the farmer.
    :type farmer_id: str
    :param attachment_id: Id of the attachment.
    :type attachment_id: str
    :return: Returns an :class:`~azure.farmbeats.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.farmbeats.core.rest.HttpRequest
    """
    api_version = "2021-03-31-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/farmers/{farmerId}/attachments/{attachmentId}')
    path_format_arguments = {
        'farmerId': _SERIALIZER.url("farmer_id", farmer_id, 'str'),
        'attachmentId': _SERIALIZER.url("attachment_id", attachment_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_download_request(
    farmer_id: str,
    attachment_id: str,
    **kwargs: Any
) -> HttpRequest:
    """Downloads and returns attachment as response for the given input filePath.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :param farmer_id: Id of the associated farmer.
    :type farmer_id: str
    :param attachment_id: Id of attachment to be downloaded.
    :type attachment_id: str
    :return: Returns an :class:`~azure.farmbeats.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.farmbeats.core.rest.HttpRequest
    """
    api_version = "2021-03-31-preview"
    accept = "application/octet-stream, application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/farmers/{farmerId}/attachments/{attachmentId}/file')
    path_format_arguments = {
        'farmerId': _SERIALIZER.url("farmer_id", farmer_id, 'str'),
        'attachmentId': _SERIALIZER.url("attachment_id", attachment_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

