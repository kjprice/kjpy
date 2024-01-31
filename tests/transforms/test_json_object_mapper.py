import unittest

import src.kjpy.transforms.transform_field_helpers as helpers
from src.kjpy.transforms.json_object_mapper import JsonObjectMapper


class TestMongoField(unittest.TestCase):
    def test_to_array(self):
        mongo_field = JsonObjectMapper("search.artists", helpers.to_array)
        self.assertEqual(mongo_field.get(""), [])
        self.assertEqual(mongo_field.return_fields, ["search.artists"])
        self.assertEqual(mongo_field.return_fields_keys, [["search", "artists"]])
