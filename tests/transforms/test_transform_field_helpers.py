from datetime import datetime
import unittest

from src.kjpy.transforms.transform_field_helpers import *


class TestMongoFieldHelpers(unittest.TestCase):
    def test_to_date(self):
        date_string = "Nov 30, 2010"
        expected_result = datetime(2010, 11, 30, 0, 0)
        result = to_date(date_string)
        self.assertEqual(result, expected_result)

    def test_array_to_string(self):
        self.assertEqual(array_to_string(["party"]), "party")

    def test_array_to_string_empty(self):
        self.assertEqual(array_to_string([]), None)

    def test_array_to_string_none(self):
        self.assertEqual(array_to_string(None), None)

    def test_array_to_string_int(self):
        self.assertEqual(array_to_string([100]), "100")

    def test_to_array(self):
        value = "Bob     Sally"
        expected_response = ["Bob", "Sally"]
        self.assertEqual(to_array(value), expected_response)

    def test_to_array_ampersand(self):
        value = "Bob & Sally"
        expected_response = ["Bob", "Sally"]
        self.assertEqual(to_array(value), expected_response)

    def test_to_array_and(self):
        value = "Bob and Sally"
        expected_response = ["Bob", "Sally"]
        self.assertEqual(to_array(value), expected_response)

    def test_to_array_slash(self):
        value = "Bob / Sally"
        expected_response = ["Bob", "Sally"]
        self.assertEqual(to_array(value), expected_response)

    def test_to_array_none(self):
        value = None
        expected_response = []
        self.assertEqual(to_array(value), expected_response)

    def test_to_array_empty(self):
        value = ""
        expected_response = []
        self.assertEqual(to_array(value), expected_response)

    def test_to_string(self):
        self.assertEqual(to_string(100), "100")

    def test_to_string_none(self):
        self.assertEqual(to_string(None), None)

    def test_handle_page_count(self):
        self.assertEqual(handle_page_count("399 pages"), 399)

    def test_handle_page_count_no_page(self):
        self.assertEqual(handle_page_count("no pages"), None)

    def test_handle_go_collect_title(self):
        title = "COMIC     Title \n\n\n Report"
        expected_response = "COMIC Title"
        self.assertEqual(handle_go_collect_title(title), expected_response)

    def test_expand_list_strings(self):
        items = ["Bob, Sara"]
        expected_response = ["Bob", "Sara"]
        self.assertEqual(expand_list_strings(items), expected_response)
