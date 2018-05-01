# coding: utf-8

"""
    Pulp3 API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class WorkersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def workers_list(self, **kwargs):  # noqa: E501
        """workers_list  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.workers_list(async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: 
        :param str name__in: Multiple values may be separated by commas.
        :param str last_heartbeat__lt: 
        :param str last_heartbeat__lte: 
        :param str last_heartbeat__gt: 
        :param str last_heartbeat__gte: 
        :param str last_heartbeat__range: Multiple values may be separated by commas.
        :param str online: 
        :param str missing: 
        :param str last_heartbeat: 
        :param str cursor: The pagination cursor value.
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.workers_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.workers_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def workers_list_with_http_info(self, **kwargs):  # noqa: E501
        """workers_list  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.workers_list_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: 
        :param str name__in: Multiple values may be separated by commas.
        :param str last_heartbeat__lt: 
        :param str last_heartbeat__lte: 
        :param str last_heartbeat__gt: 
        :param str last_heartbeat__gte: 
        :param str last_heartbeat__range: Multiple values may be separated by commas.
        :param str online: 
        :param str missing: 
        :param str last_heartbeat: 
        :param str cursor: The pagination cursor value.
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'name__in', 'last_heartbeat__lt', 'last_heartbeat__lte', 'last_heartbeat__gt', 'last_heartbeat__gte', 'last_heartbeat__range', 'online', 'missing', 'last_heartbeat', 'cursor']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workers_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'name__in' in params:
            query_params.append(('name__in', params['name__in']))  # noqa: E501
        if 'last_heartbeat__lt' in params:
            query_params.append(('last_heartbeat__lt', params['last_heartbeat__lt']))  # noqa: E501
        if 'last_heartbeat__lte' in params:
            query_params.append(('last_heartbeat__lte', params['last_heartbeat__lte']))  # noqa: E501
        if 'last_heartbeat__gt' in params:
            query_params.append(('last_heartbeat__gt', params['last_heartbeat__gt']))  # noqa: E501
        if 'last_heartbeat__gte' in params:
            query_params.append(('last_heartbeat__gte', params['last_heartbeat__gte']))  # noqa: E501
        if 'last_heartbeat__range' in params:
            query_params.append(('last_heartbeat__range', params['last_heartbeat__range']))  # noqa: E501
        if 'online' in params:
            query_params.append(('online', params['online']))  # noqa: E501
        if 'missing' in params:
            query_params.append(('missing', params['missing']))  # noqa: E501
        if 'last_heartbeat' in params:
            query_params.append(('last_heartbeat', params['last_heartbeat']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/workers/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20010',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def workers_read(self, id, **kwargs):  # noqa: E501
        """workers_read  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.workers_read(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: A UUID string identifying this worker. (required)
        :return: Worker
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.workers_read_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.workers_read_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def workers_read_with_http_info(self, id, **kwargs):  # noqa: E501
        """workers_read  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.workers_read_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: A UUID string identifying this worker. (required)
        :return: Worker
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workers_read" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `workers_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/workers/{id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Worker',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
