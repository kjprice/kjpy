import unittest

from src.kjpy.transforms.transform_deep_object import RecordHandler
from src.kjpy.transforms.json_object_mapper import JsonObjectMapper

# TODO: Create test for transforming object

original_object = {
    "name": "Bob",
    "other_info": {
        "phoneNumber": 111,
        #  "tags": ["accountant", "balding"]
    },
    "meatadata": "Copyright",
}

expected_output = {"name": "Bob", "phone": 111}

fields_map = {
    "name": JsonObjectMapper("name"),
    "other_info": {
        "phoneNumber": JsonObjectMapper("phone"),
    },
}
fields_to_ignore = ["meatadata"]


class TestTransformDeepObject(unittest.TestCase):
    def test_record_handler(self):
        record_handler = RecordHandler(
            original_object, fields_map, fields_to_ignore=fields_to_ignore
        )
        self.assertEqual(record_handler.response, expected_output)