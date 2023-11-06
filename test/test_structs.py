"""Test the structs module"""

from unittest import TestCase
from src.utils.structs import (
    Node,
    LinkedList,
)


class TestStructs(TestCase):
    """structs module unit tests"""

    def test_node_easy(self) -> None:
        """test Node class"""
        test_node = Node()
        self.assertIsNone(test_node.data)
        self.assertIsNone(test_node.link)
        self.assertEqual("None", str(test_node))

    def test_llist_easy(self) -> None:
        """test the LinkedList class"""
        # create test llist
        test_llist = LinkedList("middle")
        self.assertEqual(["middle"], [str(_) for _ in test_llist])

    def test_llist_add_remove(self) -> None:
        """test the ability to add and remove nodes from the llist"""

        test_llist = LinkedList("middle")

        # add nodes
        test_llist.append_left("start")
        test_llist.append_right("end")
        test_llist.append_left("real start")
        test_llist.append_right("real end")
        self.assertEqual("<real start, start, middle, end, real end>", str(test_llist))
        self.assertEqual(["real start", "start", "middle", "end", "real end"], [str(node) for node in test_llist])

        # remove nodes
        test_llist.remove_node("real start")
        test_llist.remove_node("real end")
        self.assertEqual("<start, middle, end>", str(test_llist))
        self.assertEqual(["start", "middle", "end"], [str(node) for node in test_llist])

        # remove node that doesn't exist
        with self.assertRaises(ValueError) as ve:
            test_llist.remove_node("value not in list")
        self.assertEqual("LList does not contain Node with data value not in list", str(ve.exception))

    def test_llist_swapping_nodes(self) -> None:
        """test the ability to swap nodes within the llist"""

        test_llist = LinkedList(data="start")
        test_llist.append_right("middle")
        test_llist.append_right("end")

        # swapping nodes
        test_llist.swap_nodes("start", "middle")
        self.assertEqual("<middle, start, end>", str(test_llist))
        test_llist.swap_nodes("start", "end")
        self.assertEqual("<middle, end, start>", str(test_llist))
        test_llist.swap_nodes("start", "middle")
        self.assertEqual("<start, end, middle>", str(test_llist))
        test_llist.swap_nodes("middle", "end")
        self.assertEqual("<start, middle, end>", str(test_llist))

        # first not present
        with self.assertRaises(ValueError) as ve:
            test_llist.swap_nodes("not in llist", "middle")
        self.assertEqual("'not in llist' not found in llist", str(ve.exception))
        # second not present
        with self.assertRaises(ValueError) as ve:
            test_llist.swap_nodes("middle", "not in llist")
        self.assertEqual("'not in llist' not found in llist", str(ve.exception))
        # both not present
        with self.assertRaises(ValueError) as ve:
            test_llist.swap_nodes("not in llist", "also not in llist")
        self.assertEqual("'not in llist' and 'also not in llist' not found in llist", str(ve.exception))
