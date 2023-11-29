"""Test the stack module"""

from unittest import TestCase

from utils.stack import Stack


class TestStack(TestCase):
    """stack module unit tests"""

    def test_empty(self) -> None:
        """test simple queue init"""
        stack = Stack()
        self.assertEqual(0, stack.size)
        self.assertIsNone(stack.top)
        self.assertTrue(stack.has_space)
        self.assertTrue(stack.is_empty)
        self.assertIsNone(stack.peek())

    def test_add_remove(self) -> None:
        """test add remove methods"""
        stack = Stack()

        # add nodes
        stack.push("test")
        self.assertEqual("test", str(stack.peek()))

        stack.push("test 2")
        self.assertEqual("test 2", str(stack.peek()))

        # remove nodes
        first_popped_value = stack.pop()
        self.assertEqual("test 2", first_popped_value)
        second_popped_value = stack.pop()
        self.assertEqual("test", second_popped_value)

    def test_underflow(self) -> None:
        """test exception when stack underflow"""
        stack = Stack(limit=1)

        # add node
        stack.push("test")

        # remove node
        test = stack.pop()
        self.assertEqual("test", test)

        # underflow stack
        with self.assertRaises(AssertionError):
            stack.pop()

    def test_overflow(self) -> None:
        """test exception when stack overflow"""

        stack = Stack(limit=1)

        # add node
        stack.push("test")

        # overflow stack
        with self.assertRaises(AssertionError):
            stack.push("overflow")
