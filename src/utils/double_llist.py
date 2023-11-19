"""double llist module"""

from __future__ import annotations
from typing import Any, Optional

from utils.node import DoublyLinkedNode


class DoublyLinkedList:
    """Doubly Linked List data structure"""

    def __init__(self) -> None:
        self._head_node: Optional[DoublyLinkedNode] = None
        self._tail_node: Optional[DoublyLinkedNode] = None

    def __str__(self) -> str:
        list_str = "<"
        current_node: Optional[DoublyLinkedNode] = self._head_node
        while current_node is not None:
            list_str += str(current_node.data)
            next_link = current_node.next_node
            if next_link is not None:
                list_str += ", "
            current_node = next_link
        list_str += ">"
        return list_str

    @property
    def head(self) -> Optional[DoublyLinkedNode]:
        """get the dllist head"""
        return self._head_node

    @property
    def tail(self) -> Optional[DoublyLinkedNode]:
        """get the dllist tail"""
        return self._tail_node

    def append_left(self, new_value: Optional[Any] = None) -> None:
        """add node to start of dllist"""
        head_node = self._head_node
        new_head = DoublyLinkedNode(data=new_value, next_node=head_node, prev_node=None)
        if head_node is not None:
            head_node.prev_node = new_head
        self._head_node = new_head
        if self._tail_node is None:
            self._tail_node = new_head

    def append_right(self, new_value: Optional[Any] = None) -> None:
        """add node to end of dllist"""
        tail_node = self._tail_node
        new_tail = DoublyLinkedNode(data=new_value, next_node=None, prev_node=tail_node)
        if tail_node is not None:
            tail_node.next_node = new_tail
        self._tail_node = new_tail
        if self._head_node is None:
            self._head_node = new_tail

    def remove_left(self) -> Optional[Any]:
        """remove node at the start of dllist"""
        removed_head = self._head_node
        if removed_head is None:
            return None
        self._head_node = removed_head.next_node
        if self._head_node is not None:
            self._head_node.prev_node = None
        if removed_head == self._tail_node:
            self.remove_right()
        return removed_head.data

    def remove_right(self) -> Optional[Any]:
        """remove node at the end of the dllist"""
        removed_tail = self._tail_node
        if removed_tail is None:
            return None
        self._tail_node = removed_tail.prev_node
        if self._tail_node is not None:
            self._tail_node.next_node = None
        if removed_tail == self._head_node:
            self.remove_left()
        return removed_tail.data

    @property
    def middle_node(self) -> Optional[DoublyLinkedNode]:
        """find the center of the llist"""
        fast_pointer: Optional[DoublyLinkedNode] = self._head_node
        slow_pointer: Optional[DoublyLinkedNode] = self._head_node
        while fast_pointer is not None:
            fast_pointer = fast_pointer.next_node
            if fast_pointer is not None and slow_pointer is not None:
                fast_pointer = fast_pointer.next_node
                slow_pointer = slow_pointer.next_node
        return slow_pointer

    def remove_middle(self) -> Optional[Any]:
        """remove node at the middle of dllist"""
        middle_node = self.middle_node
        if middle_node is not None:
            if middle_node.prev_node is None:
                self.remove_left()
            elif middle_node.next_node is None:
                self.remove_right()
            else:
                middle_node.prev_node.next_node = middle_node.next_node
                middle_node.next_node.prev_node = middle_node.prev_node
            return middle_node.data
        return None

    def remove_by_value(self, value: Any) -> Optional[Any]:
        """remove node by value"""
        node_to_remove = None
        current_node: Optional[DoublyLinkedNode] = self._head_node
        while current_node is not None:
            if current_node.data == value:
                node_to_remove = current_node
                break
            current_node = current_node.next_node
        if node_to_remove is None:
            return None
        if node_to_remove == self._head_node:
            return self.remove_left()
        if node_to_remove == self._tail_node:
            return self.remove_right()
        next_node = node_to_remove.next_node
        prev_node = node_to_remove.prev_node
        if prev_node is not None:
            prev_node.next_node = next_node
        if next_node is not None:
            next_node.prev_node = prev_node
        return node_to_remove.data
