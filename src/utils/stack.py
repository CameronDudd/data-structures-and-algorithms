"""Stacks (LIFO)"""

from typing import Any, Optional

from utils.node import Node


class Stack:
    """Stack data structure"""

    def __init__(self, limit: int = 1000) -> None:
        self._size = 0
        self.limit = limit
        self._top: Optional[Node] = None

    @property
    def size(self) -> int:
        """current size of stack"""
        return self._size

    @property
    def top(self) -> Optional[Any]:
        """top of the stack"""
        return self._top

    @property
    def has_space(self) -> bool:
        """stack has space"""
        return self.size < self.limit

    @property
    def is_empty(self) -> bool:
        """stack is empty"""
        return self.size == 0

    def push(self, value: Optional[Any]) -> None:
        """push item onto the stack"""
        item = Node(value)
        item.next_node = self._top
        self._top = item
        self._size += 1

    def pop(self) -> Any:
        """pop item off of the stack"""
        item_to_remove = self._top
        assert item_to_remove is not None
        self._top = item_to_remove.next_node
        self._size -= 1
        return item_to_remove.data

    def peek(self) -> Optional[Any]:
        """return top of stack"""
        return self.top
