"""Test the queue module"""

from unittest import TestCase

from utils.queue import Queue


class TestQueue(TestCase):
    """queue module unit tests"""

    def test_empty(self) -> None:
        """test simple queue init"""
        queue = Queue()
        self.assertEqual(0, queue.size)
        self.assertTrue(queue.empty)
        self.assertTrue(queue.has_space)
        self.assertIsNone(queue.peek())

    def test_add_remove(self) -> None:
        """test add remove methods"""
        queue = Queue(3)

        # adding
        queue.enqueue("test")
        self.assertEqual("test", queue.peek())
        self.assertEqual(queue.size, 1)

        queue.enqueue("test 2")
        self.assertEqual("test", queue.peek())
        self.assertEqual(queue.size, 2)

        self.assertEqual("test > test 2 > ", str(queue))

        # removing
        first_removed = queue.dequeue()
        self.assertEqual(1, queue.size)
        self.assertEqual("test", first_removed)
        self.assertEqual("test 2", queue.peek())

        second_removed = queue.dequeue()
        self.assertEqual(0, queue.size)
        self.assertEqual("test 2", second_removed)

    def test_overflow(self) -> None:
        """test queue exception when overflowed"""
        for limit_size in range(100):
            queue = Queue(limit_size)
            with self.assertRaises(AssertionError):
                for _ in range(limit_size + 1):
                    queue.enqueue()

    def test_underflow(self) -> None:
        """test queue exception when underflowed"""
        for limit_size in range(100):
            queue = Queue(limit_size)
            for _ in range(limit_size):
                queue.enqueue()
            with self.assertRaises(AssertionError):
                for _ in range(limit_size + 1):
                    queue.dequeue()
