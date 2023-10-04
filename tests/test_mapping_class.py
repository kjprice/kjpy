import unittest
from src.kjpy.collections.mapping_class import MappingAbstract


class MappingOverwrite(MappingAbstract[str, str]):
    pass


class TestMappingAbstract(unittest.TestCase):
    def test_addone(self):
        mapping = MappingOverwrite()
        mapping["test"] = "kj"
        self.assertEqual(mapping["test"], "kj")
        # self.assertEqual(average([]), 0)
