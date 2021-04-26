# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import TYPE_CHECKING

from azure.core.pipeline.transport._base import _format_url_section
from azure.farmbeats.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, List, Optional

_SERIALIZER = Serializer()


def build_list_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Returns a paginated list of scene resources.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword farmer_id: FarmerId.
    :paramtype farmer_id: str
    :keyword boundary_id: BoundaryId.
    :paramtype boundary_id: str
    :keyword provider: Provider name of scene data.
    :paramtype provider: str
    :keyword source: Source name of scene data, default value Sentinel_2_L2A (Sentinel 2 L2A).
    :paramtype source: str
    :keyword start_date_time: Scene start UTC datetime (inclusive), sample format: yyyy-MM-
     ddThh:mm:ssZ.
    :paramtype start_date_time: ~datetime.datetime
    :keyword end_date_time: Scene end UTC datetime (inclusive), sample format: yyyy-MM-dThh:mm:ssZ.
    :paramtype end_date_time: ~datetime.datetime
    :keyword max_cloud_coverage_percentage: Filter scenes with cloud coverage percentage less than
     max value. Range [0 to 100.0].
    :paramtype max_cloud_coverage_percentage: float
    :keyword max_dark_pixel_coverage_percentage: Filter scenes with dark pixel coverage percentage
     less than max value. Range [0 to 100.0].
    :paramtype max_dark_pixel_coverage_percentage: float
    :keyword image_names: List of image names to be filtered.
    :paramtype image_names: list[str]
    :keyword image_resolutions: List of image resolutions in meters to be filtered.
    :paramtype image_resolutions: list[float]
    :keyword image_formats: List of image formats to be filtered.
    :paramtype image_formats: list[str]
    :keyword max_page_size: Maximum number of items needed (inclusive).
     Minimum = 10, Maximum = 1000, Default value = 50.
    :paramtype max_page_size: int
    :keyword skip_token: Skip token for getting next set of results.
    :paramtype skip_token: str
    :return: Returns an :class:`~azure.farmbeats.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.farmbeats.core.rest.HttpRequest
    """
    farmer_id = kwargs.pop('farmer_id')  # type: str
    boundary_id = kwargs.pop('boundary_id')  # type: str
    provider = kwargs.pop('provider', "Microsoft")  # type: str
    source = kwargs.pop('source', "Sentinel_2_L2A")  # type: Optional[str]
    start_date_time = kwargs.pop('start_date_time', None)  # type: Optional[datetime.datetime]
    end_date_time = kwargs.pop('end_date_time', None)  # type: Optional[datetime.datetime]
    max_cloud_coverage_percentage = kwargs.pop('max_cloud_coverage_percentage', 100)  # type: Optional[float]
    max_dark_pixel_coverage_percentage = kwargs.pop('max_dark_pixel_coverage_percentage', 100)  # type: Optional[float]
    image_names = kwargs.pop('image_names', None)  # type: Optional[List[str]]
    image_resolutions = kwargs.pop('image_resolutions', None)  # type: Optional[List[float]]
    image_formats = kwargs.pop('image_formats', None)  # type: Optional[List[str]]
    max_page_size = kwargs.pop('max_page_size', 50)  # type: Optional[int]
    skip_token = kwargs.pop('skip_token', None)  # type: Optional[str]
    api_version = "2021-03-31-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/scenes')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['provider'] = _SERIALIZER.query("provider", provider, 'str')
    query_parameters['farmerId'] = _SERIALIZER.query("farmer_id", farmer_id, 'str')
    query_parameters['boundaryId'] = _SERIALIZER.query("boundary_id", boundary_id, 'str')
    if source is not None:
        query_parameters['source'] = _SERIALIZER.query("source", source, 'str')
    if start_date_time is not None:
        query_parameters['startDateTime'] = _SERIALIZER.query("start_date_time", start_date_time, 'iso-8601')
    if end_date_time is not None:
        query_parameters['endDateTime'] = _SERIALIZER.query("end_date_time", end_date_time, 'iso-8601')
    if max_cloud_coverage_percentage is not None:
        query_parameters['maxCloudCoveragePercentage'] = _SERIALIZER.query("max_cloud_coverage_percentage", max_cloud_coverage_percentage, 'float', maximum=100, minimum=0)
    if max_dark_pixel_coverage_percentage is not None:
        query_parameters['maxDarkPixelCoveragePercentage'] = _SERIALIZER.query("max_dark_pixel_coverage_percentage", max_dark_pixel_coverage_percentage, 'float', maximum=100, minimum=0)
    if image_names is not None:
        query_parameters['imageNames'] = [_SERIALIZER.query("image_names", q, 'str') if q is not None else '' for q in image_names]
    if image_resolutions is not None:
        query_parameters['imageResolutions'] = [_SERIALIZER.query("image_resolutions", q, 'float') if q is not None else '' for q in image_resolutions]
    if image_formats is not None:
        query_parameters['imageFormats'] = [_SERIALIZER.query("image_formats", q, 'str') if q is not None else '' for q in image_formats]
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


def build_create_satellite_data_ingestion_job_request(
    job_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Create a satellite data ingestion job.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :param job_id: JobId provided by user.
    :type job_id: str
    :keyword json: Job parameters supplied by user.
    :paramtype json: Any
    :keyword content: Job parameters supplied by user.
    :paramtype content: Any
    :return: Returns an :class:`~azure.farmbeats.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.farmbeats.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "boundaryId": "str",
                "data": {
                    "imageFormats": [
                        "str (optional)"
                    ],
                    "imageNames": [
                        "str (optional)"
                    ],
                    "imageResolutions": [
                        "float (optional)"
                    ]
                },
                "description": "str (optional)",
                "endDateTime": "datetime",
                "farmerId": "str",
                "name": "str (optional)",
                "properties": {
                    "str": "object (optional)"
                },
                "provider": "str (optional)",
                "source": "str (optional)",
                "startDateTime": "datetime"
            }
    """
    content_type = kwargs.pop("content_type", None)
    api_version = "2021-03-31-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/scenes/satellite/ingest-data/{jobId}')
    path_format_arguments = {
        'jobId': _SERIALIZER.url("job_id", job_id, 'str'),
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
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_satellite_data_ingestion_job_details_request(
    job_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get satellite data ingestion job's details.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :param job_id: Id of the job.
    :type job_id: str
    :return: Returns an :class:`~azure.farmbeats.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.farmbeats.core.rest.HttpRequest
    """
    api_version = "2021-03-31-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/scenes/satellite/ingest-data/{jobId}')
    path_format_arguments = {
        'jobId': _SERIALIZER.url("job_id", job_id, 'str'),
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


def build_download_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Downloads and returns file content as response for the given input filePath.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword file_path: cloud storage path of scene file.
    :paramtype file_path: str
    :return: Returns an :class:`~azure.farmbeats.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.farmbeats.core.rest.HttpRequest
    """
    file_path = kwargs.pop('file_path')  # type: str
    api_version = "2021-03-31-preview"
    accept = "application/octet-stream, application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/scenes/downloadFiles')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['filePath'] = _SERIALIZER.query("file_path", file_path, 'str')
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

