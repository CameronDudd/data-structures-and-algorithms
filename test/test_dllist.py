"""Test the double_llist module"""

from unittest import TestCase
from src.utils.double_llist import (
    DoubleNode,
    DoublyLinkedList,
)


class TestDoublyLlist(TestCase):
    """double_llist module unit tests"""

    def test_double_node_easy(self) -> None:
        """test DoubleNode class"""
        test_dnode = DoubleNode()
        self.assertIsNone(test_dnode.data)
        self.assertIsNone(test_dnode.next)
        self.assertIsNone(test_dnode.prev)
        self.assertEqual("<-None->", str(test_dnode))

    def test_dllist_easy(self) -> None:
        """test DoublyLinkedList class"""
        # create test dllist
        test_dllist = DoublyLinkedList("middle")
        self.assertEqual("middle", test_dllist.head.data)
        self.assertIsNone(test_dllist.head.next)
        self.assertIsNone(test_dllist.head.prev)
        self.assertEqual("<middle>", str(test_dllist))

    def test_empty_dllist(self) -> None:
        """test dllist methods when initialized with nothing"""

        test_dllist = DoublyLinkedList()
        test_dllist.append_left()
        test_dllist.append_right()
        self.assertEqual("<None, None, None>", str(test_dllist))

        # remove nodes left
        test_dllist.remove_left()
        self.assertEqual("<None, None>", str(test_dllist))

        test_dllist.remove_left()
        self.assertEqual("<None>", str(test_dllist))

        test_dllist.remove_left()
        self.assertEqual("<None>", str(test_dllist))

        test_dllist = DoublyLinkedList()
        test_dllist.append_left()
        test_dllist.append_right()
        self.assertEqual("<None, None, None>", str(test_dllist))

        # remove nodes right
        test_dllist.remove_right()
        self.assertEqual("<None, None>", str(test_dllist))

        test_dllist.remove_right()
        self.assertEqual("<None>", str(test_dllist))

        test_dllist.remove_right()
        self.assertEqual("<None>", str(test_dllist))

    def test_dllist_add_remove(self) -> None:
        """test the ability to add and remove double nodes from the dllist"""

        test_dllist = DoublyLinkedList("middle")

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

        return
        # todo
        # remove middle node
        test_dllist.remove_middle()
        self.assertEqual("<start, end>", str(test_dllist))
