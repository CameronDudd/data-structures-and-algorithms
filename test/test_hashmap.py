"""Test the hash module"""

from unittest import TestCase
from utils.hashmap import HashMap


class TestHashMap(TestCase):
    """hash module unit tests"""

    def test_hash_easy(self) -> None:
        """easy hash module test"""
        hash_map = HashMap(20)
        hash_map.assign("gneiss", "metamorphic")
        retrieved_value = hash_map.retrieve("gneiss")
        self.assertEqual("metamorphic", retrieved_value)

        hash_map["test_key"] = "test_value"
        self.assertEqual("test_value", hash_map["test_key"])

    def test_hash_conflict(self) -> None:
        """test keys producing same hash"""
        hash_map = HashMap(15)
        hash_map["gabbro"] = "igneous"
        hash_map["sandstone"] = "sedimentary"
        hash_map["gneiss"] = "metamorphic"
        self.assertEqual("igneous", hash_map["gabbro"])
        self.assertEqual("sedimentary", hash_map["sandstone"])
        self.assertEqual("metamorphic", hash_map["gneiss"])
