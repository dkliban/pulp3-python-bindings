# coding: utf-8

"""
    Pulp3 API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.status_api import StatusApi  # noqa: E501
from swagger_client.rest import ApiException


class TestStatusApi(unittest.TestCase):
    """StatusApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.status_api.StatusApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_status_list(self):
        """Test case for status_list

        """
        pass


if __name__ == '__main__':
    unittest.main()