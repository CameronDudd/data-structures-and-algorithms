"""Test the llist module"""

from unittest import TestCase
from utils.node import Node
from utils.llist import LinkedList


class TestLlist(TestCase):
    """llist module unit tests"""

    def test_node_easy(self) -> None:
        """test Node class"""
        test_node = Node()
        self.assertIsNone(test_node.data)
        self.assertIsNone(test_node.next_node)
        self.assertEqual("None > ", str(test_node))

    def test_llist_easy(self) -> None:
        """test the LinkedList class"""
        # create test llist
        test_llist = LinkedList()
        test_llist.append_left("middle")
        self.assertEqual("middle > ", str(test_llist.head))
        assert test_llist.head is not None, "test_llist.next_node should not be None"
        self.assertIsNone(test_llist.head.next_node)
        self.assertEqual("<middle>", str(test_llist))

    def test_llist_add_remove(self) -> None:
        """test the ability to add and remove nodes from the llist"""

        test_llist = LinkedList()

        # add nodes
        test_llist.append_left("middle")
        test_llist.append_left("start")
        test_llist.append_right("end")
        test_llist.append_left("real start")
        test_llist.append_right("real end")
        self.assertEqual("<real start, start, middle, end, real end>", str(test_llist))

        # remove nodes
        test_llist.remove_node("real start")
        test_llist.remove_node("real end")
        self.assertEqual("<start, middle, end>", str(test_llist))

        # remove node that doesn't exist
        with self.assertRaises(ValueError) as ve:
            test_llist.remove_node("value not in list")
        self.assertEqual("value not in list not found in llist", str(ve.exception))

    def test_llist_swapping_nodes(self) -> None:
        """test the ability to swap nodes within the llist"""

        test_llist = LinkedList()
        test_llist.append_left("start")
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

    def test_llist_nth_last_node(self) -> None:
        """test llist nth last node"""
        llist = LinkedList()
        llist.append_left(0)
        llist.append_right(1)
        llist.append_right(2)
        llist.append_right(3)
        llist.append_right(4)

        last_node = llist.nth_last_node(0)
        self.assertEqual(4, last_node.data)
        first_to_last_node = llist.nth_last_node(1)
        self.assertEqual(3, first_to_last_node.data)
        second_to_last_node = llist.nth_last_node(2)
        self.assertEqual(2, second_to_last_node.data)
        third_to_last_node = llist.nth_last_node(3)
        self.assertEqual(1, third_to_last_node.data)
        fourth_to_last_node = llist.nth_last_node(4)
        self.assertEqual(0, fourth_to_last_node.data)
        with self.assertRaises(ValueError) as ve:
            llist.nth_last_node(5)
        self.assertEqual("nth_last_pointer None", str(ve.exception))

    def test_llist_middle_node(self) -> None:
        """test llist llist middle node"""
        llist = LinkedList()

        # 0
        llist.append_left(0)
        self.assertEqual("0 > ", str(llist.middle_node))

        # 0 -> 1
        llist.append_right(1)
        self.assertEqual("1 > ", str(llist.middle_node))

        # 0 -> 1 -> 2
        llist.append_right(2)
        self.assertEqual("1 > ", str(llist.middle_node))

        # 0 -> 1 -> 2 -> 3
        llist.append_right(3)
        self.assertEqual("2 > ", str(llist.middle_node))

        # 0 -> 1 -> 2 -> 3 -> 4
        llist.append_right(4)
        self.assertEqual("2 > ", str(llist.middle_node))

        # 0 -> 1 -> 2 -> 3 -> 4 -> 5
        llist.append_right(5)
        self.assertEqual("3 > ", str(llist.middle_node))
