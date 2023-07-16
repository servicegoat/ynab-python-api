# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import ynab_api
from ynab_api.models.save_category_response_data import SaveCategoryResponseData  # noqa: E501
from ynab_api.rest import ApiException


class TestSaveCategoryResponseData(unittest.TestCase):
    """SaveCategoryResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSaveCategoryResponseData(self):
        """Test SaveCategoryResponseData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ynab_api.models.save_category_response_data.SaveCategoryResponseData()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
