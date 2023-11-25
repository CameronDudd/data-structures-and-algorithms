"""Queues"""

from typing import Optional, Any

from utils.node import Node


class Queue:
    """Queue data structure"""

    def __init__(self, max_size: Optional[int] = None) -> None:
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size = 0
        self.max_size = max_size

    @property
    def size(self) -> int:
        """return size of queue"""
        return self._size

    @property
    def empty(self) -> bool:
        """return queue is empty"""
        return self._size == 0

    @property
    def has_space(self) -> bool:
        """return queue has space"""
        if self.max_size is None:
            return True
        return self.size < self.max_size

    def peek(self) -> Optional[Any]:
        """look at the value at the head of the queue"""
        if self.empty:
            return None
        return None if self._head is None else self._head.data

    def enqueue(self, value: Optional[Any] = None) -> None:
        """add to head of queue"""
        if self.has_space:
            item_to_add = Node(value)
            if self.empty:
                self._head = item_to_add
                self._tail = item_to_add
            else:
                assert self._tail is not None
                self._tail.next_node = item_to_add
                self._tail = item_to_add
            self._size += 1
