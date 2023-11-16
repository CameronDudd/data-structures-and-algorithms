"""double llist module"""

from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass


@dataclass
class DoubleNode:
    """Doubly linked Node data structure"""

    data: Optional[Any] = None
    prev: Optional[Any] = None
    next: Optional[Any] = None

    def __str__(self) -> str:
        prev_ = "" if self.prev is None else self.prev.data
        next_ = "" if self.next is None else self.next.data
        return f"{prev_} <- {self.data} -> {next_}"


class DoublyLinkedList:
    """Doubly Linked List data structure"""

    def __init__(self, data: Any = None, next_: Optional[DoubleNode] = None, prev_: Optional[DoubleNode] = None) -> None:
        # fixme: add tail node
        self._head_node: DoubleNode = DoubleNode(data, prev_, next_)

    def __str__(self) -> str:
        list_str = "<"
        current_node: Optional[DoubleNode] = self._head_node
        while current_node is not None:
            list_str += str(current_node.data)
            next_link = current_node.next
            if next_link is not None:
                list_str += ", "
            current_node = next_link
        list_str += ">"
        return list_str

    @property
    def head(self) -> DoubleNode:
        """get the dllist head"""
        return self._head_node

    def append_left(self, value: Optional[Any] = None) -> None:
        """add node to start of dllist"""

        new_node = DoubleNode(value, None, self._head_node)
        self._head_node.prev = new_node
        self._head_node = new_node

    def append_right(self, value: Optional[Any] = None) -> None:
        """add node to end of dllist"""
        new_node = DoubleNode(value, None, None)
        current_node = self._head_node
        while current_node.next is not None:
            current_node = current_node.next
        new_node.prev = current_node
        current_node.next = new_node

    def remove_left(self) -> None:
        """remove node at the start of dllist"""
        current_head = self._head_node
        current_head_next = DoubleNode() if current_head.next is None else current_head.next
        current_head_next.prev = None
        self._head_node = current_head_next

    def remove_right(self) -> None:
        """remove node at the end of dllist"""
        current_node = self._head_node
        while current_node.next is not None:
            current_node = current_node.next
        before_last = current_node.prev
        if before_last is None:  # at head of dllist
            self._head_node = DoubleNode()
        else:
            before_last.next = None

            before_last.next = None

    @property
    def middle_node(self) -> Optional[DoubleNode]:
        """find the center of the dllist"""
        fast_pointer: Optional[DoubleNode] = self._head_node
        slow_pointer: Optional[DoubleNode] = self._head_node
        while fast_pointer is not None:
            fast_pointer = fast_pointer.next
            if fast_pointer is not None and slow_pointer is not None:
                fast_pointer = fast_pointer.next
                slow_pointer = slow_pointer.next
        return slow_pointer

    def remove_middle(self) -> None:
        """remove node at the middle of dllist"""
        middle_node = self.middle_node
        if middle_node is not None:
            if middle_node.next is None or middle_node.prev is None:
                # middle is start/end therefore remove
                self.remove_left()
            else:
                middle_node.prev.next = middle_node.next
                middle_node.next.prev = middle_node.prev

    def remove_by_value(self, value: Any) -> None:
        """remove node by value"""
        node_to_remove = None
        current_node: Optional[DoubleNode] = self._head_node
        while current_node is not None:
            if current_node.data == value:
                node_to_remove = current_node
                break
            current_node = current_node.next
        if node_to_remove is None:
            return
        if node_to_remove == self._head_node:
            self.remove_left()
        elif node_to_remove.next is None:
            self.remove_right()
        elif node_to_remove is not None:
            next_node = node_to_remove.next
            prev_node = node_to_remove.prev
            if prev_node is not None:
                prev_node.next = next_node
            if next_node is not None:
                next_node.prev = prev_node
