"""Test the double_llist module"""

from unittest import TestCase
from utils.node import DoublyLinkedNode
from utils.double_llist import DoublyLinkedList


class TestDoublyLlist(TestCase):
    """double_llist module unit tests"""

    def test_double_node_easy(self) -> None:
        """test DoubleNode class"""
        test_dnode = DoublyLinkedNode()
        self.assertIsNone(test_dnode.data)
        self.assertIsNone(test_dnode.next_node)
        self.assertIsNone(test_dnode.prev_node)
        self.assertEqual("None", str(test_dnode))

    def test_dllist_easy(self) -> None:
        """test DoublyLinkedList class"""
        # create test dllist
        test_dllist = DoublyLinkedList()
        self.assertEqual("<>", str(test_dllist))

        test_dllist.append_left("middle")

        self.assertEqual("middle", str(test_dllist.head))
        self.assertEqual("middle", str(test_dllist.tail))

        assert test_dllist.head is not None, "test_dllist.head should not be None"
        assert test_dllist.tail is not None, "test_dllist.tail should not be None"

        self.assertIsNone(test_dllist.head.next_node)
        self.assertIsNone(test_dllist.tail.next_node)
        self.assertIsNone(test_dllist.head.prev_node)
        self.assertIsNone(test_dllist.tail.prev_node)
        self.assertEqual("<middle>", str(test_dllist))

    def test_empty_dllist(self) -> None:
        """test dllist methods when initialized with nothing"""

        test_dllist = DoublyLinkedList()
        test_dllist.append_left()
        self.assertEqual("<None>", str(test_dllist))
        test_dllist.append_left()
        self.assertEqual("<None, None>", str(test_dllist))
        test_dllist.append_right()
        self.assertEqual("<None, None, None>", str(test_dllist))

        # remove nodes left
        test_dllist.remove_left()
        self.assertEqual("<None, None>", str(test_dllist))

        test_dllist.remove_left()
        self.assertEqual("<None>", str(test_dllist))

        test_dllist.remove_left()
        self.assertEqual("<>", str(test_dllist))

        test_dllist.append_left()
        test_dllist.append_right()
        self.assertEqual("<None, None>", str(test_dllist))

        # remove nodes right
        val = test_dllist.remove_right()
        self.assertIsNone(val)
        self.assertEqual("<None>", str(test_dllist))

        test_dllist.remove_right()
        self.assertEqual("<>", str(test_dllist))

        test_dllist.remove_right()
        self.assertEqual("<>", str(test_dllist))

    def test_dllist_add_remove(self) -> None:
        """test the ability to add and remove double nodes from the dllist"""

        test_dllist = DoublyLinkedList()
        test_dllist.append_left("middle")

        # add nodes
        test_dllist.append_left("start")
        test_dllist.append_right("end")
        test_dllist.append_left("real start")
        test_dllist.append_right("real end")
        self.assertEqual("<real start, start, middle, end, real end>", str(test_dllist))

        # remove nodes
        test_dllist.remove_left()
        test_dllist.remove_right()
        self.assertEqual("<start, middle, end>", str(test_dllist))

        # remove middle node
        test_dllist.remove_middle()
        self.assertEqual("<start, end>", str(test_dllist))

        test_dllist.remove_middle()
        self.assertEqual("<start>", str(test_dllist))

        test_dllist.remove_middle()
        self.assertEqual("<>", str(test_dllist))

    def test_dllist_remove_by_value(self) -> None:
        """test the ability to remove double nodes from the dllist by value"""

        test_dllist = DoublyLinkedList()
        test_dllist.append_left("middle")

        # add nodes
        test_dllist.append_left("start")
        test_dllist.append_right("end")
        test_dllist.append_left("real start")
        test_dllist.append_right("real end")
        self.assertEqual("<real start, start, middle, end, real end>", str(test_dllist))

        test_dllist.remove_by_value("start")
        self.assertEqual("<real start, middle, end, real end>", str(test_dllist))

        test_dllist.remove_by_value(None)
        self.assertEqual("<real start, middle, end, real end>", str(test_dllist))

        test_dllist.remove_by_value("middle")
        self.assertEqual("<real start, end, real end>", str(test_dllist))

        test_dllist.remove_by_value("real end")
        self.assertEqual("<real start, end>", str(test_dllist))
