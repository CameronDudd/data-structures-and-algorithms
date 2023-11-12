"""double llist module"""

from __future__ import annotations
from typing import Any, Optional


class DoubleNode:
    """Doubly linked Node data structure"""

    # pylint: disable=too-few-public-methods

    def __init__(self, data: Any = None, previous_link: Optional[DoubleNode] = None, next_link: Optional[DoubleNode] = None) -> None:
        self.data = data
        self.prev = previous_link
        self.next = next_link

    def __str__(self) -> str:
        prev = "" if self.prev is None else self.prev.data
        next = "" if self.next is None else self.next.data
        return f"{prev}<-{self.data}->{next}"


class DoublyLinkedList:
    """Doubly Linked List data structure"""

    def __init__(self, data: Any = None, next_link: Optional[DoubleNode] = None, prev_link: Optional[DoubleNode] = None) -> None:
        self._head_node: DoubleNode = DoubleNode(data=data, next_link=next_link, previous_link=prev_link)

    def __iter__(self) -> DoublyLinkedList:
        """todo"""

    def __next__(self) -> DoubleNode:
        """todo"""

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
        new_node = DoubleNode(data=value, next_link=self._head_node, previous_link=None)
        self._head_node = new_node

    def append_right(self, value: Optional[Any] = None) -> None:
        """add node to end of dllist"""
        new_node = DoubleNode(data=value, next_link=None, previous_link=None)
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
        # todo
        return
        middle_node = self.middle_node
        if middle_node is not None:
            if middle_node.next is None or middle_node.prev is None:
                # middle is start/end therefore remove
                self.remove_left()
            else:
                middle_node.prev.next = middle_node.next
                middle_node.next.prev = middle_node.prev