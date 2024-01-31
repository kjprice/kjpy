from datetime import datetime
from typing import List
import unittest

from src.kjpy.transforms.transform_field_helpers import *


class TestRecursiveCurrentObject(unittest.TestCase):
    @property
    def obj(self):
        return {"Bob": {"Sara": True}}

    def helper(self, items: List[str], expect_change=False):
        obj = self.obj
        new_obj = get_recursive_current_object(obj, items)
        if expect_change:
            self.assertNotEqual(obj, self.obj)
        else:
            self.assertEqual(obj, self.obj)

        return new_obj

    def test_get_recursive_current_object(self):
        sara_obj = {"Sara": True}
        self.assertEqual(self.helper(["Bob", "Sara"]), sara_obj)
        self.assertEqual(self.helper(["Bob", "Tom"]), sara_obj)
        self.assertEqual(self.helper(["Bob", "Tom", "Jerry"], True), {})


class TestSetObjFromKey(unittest.TestCase):
    @property
    def obj(self):
        return {"Bob": "Tom", "Sara": ["Jim"]}

    def helper(self, key: str, value):
        obj = self.obj
        set_obj_from_key_map(obj, key, value)
        return obj

    def test_set_obj_from_key_map(self):
        self.assertEqual(self.helper("tom", "jerry"), {**self.obj, "tom": "jerry"})
        print(self.helper("Bob", "jerry"))
        self.assertEqual(self.helper("Bob", "jerry"), {**self.obj, "Bob": "jerry"})
        self.assertEqual(
            self.helper("Sara", "jerry"), {**self.obj, "Sara": ["Jim", "jerry"]}
        )
        self.assertEqual(
            self.helper("Sara", ["jerry", "john"]),
            {**self.obj, "Sara": ["Jim", "jerry", "john"]},
        )


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
