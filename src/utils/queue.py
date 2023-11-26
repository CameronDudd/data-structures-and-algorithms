"""Queues (FIFO)"""

from typing import Optional, Any

from utils.node import Node


class Queue:
    """Queue data structure"""

    def __init__(self, max_size: Optional[int] = None) -> None:
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size = 0
        self.max_size = max_size

    def __str__(self) -> str:
        str_ = ""
        current_node = self._head
        while current_node is not None:
            str_ += f"{str(current_node)} > "
            current_node = current_node.next_node
        return str_

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
        assert self.has_space
        item_to_add = Node(value)
        if self.empty:
            self._head = item_to_add
            self._tail = item_to_add
        else:
            assert self._tail is not None
            self._tail.next_node = item_to_add
            self._tail = item_to_add
        self._size += 1

    def dequeue(self) -> Optional[Any]:
        """remove from the head of the queue"""
        assert not self.empty
        item_to_remove = self._head
        if self.size == 1:
            self._head = None
            self._tail = None
        else:
            assert self._head is not None
            self._head = self._head.next_node
        self._size -= 1
        return None if item_to_remove is None else item_to_remove.data
