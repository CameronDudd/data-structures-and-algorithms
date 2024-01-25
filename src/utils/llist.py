"""llist module"""

from __future__ import annotations
from typing import Any, Optional, Tuple

from utils.node import Node


class LinkedList:
    """Linked List data structure"""

    def __init__(self) -> None:
        self._head_node: Optional[Node] = None

    def __str__(self) -> str:
        list_str = "<"
        current_node: Optional[Node] = self._head_node
        while current_node is not None:
            if current_node.data is not None:
                list_str += str(current_node.data)
            current_link = current_node.next_node
            if current_link is not None:
                list_str += ", "
            current_node = current_link
        list_str += ">"
        return list_str

    @property
    def head(self) -> Optional[Node]:
        """get head node"""
        return self._head_node

    def remove_node(self, value: Any) -> Optional[Any]:
        """remove first node in list with matching value"""
        current_node = self._head_node
        if current_node is None:
            return None
        if current_node.data == value:
            self._head_node = current_node.next_node
            return current_node.data

        while current_node is not None:
            next_node = current_node.next_node
            if next_node is None:
                break  # reached the end of the list
            if next_node.data == value:
                current_node.next_node = next_node.next_node
                current_node = None
            else:
                current_node = next_node
        if next_node is None:
            raise ValueError(f"{value} not found in llist")
        return next_node.data

    def append_left(self, new_value: Any) -> None:
        """add node to start of llist"""
        new_node = Node(data=new_value, next_node=self._head_node)
        self._head_node = new_node

    def append_right(self, value: Any) -> None:
        """add node to end of llist"""
        new_node = Node(data=value, next_node=None)
        current_node = self._head_node
        if current_node is None:
            self._head_node = new_node
            return
        next_node = current_node.next_node
        while next_node is not None:
            current_node = next_node
            next_node = next_node.next_node
        if current_node is not None:
            current_node.next_node = new_node

    def _find_nodes_for_swp(self, val: Any) -> Tuple[Optional[Node], Optional[Node]]:
        """find a node containing val and return said node with preceeding node"""
        node: Optional[Node] = self._head_node
        prev_node = None
        # find node
        while node is not None:
            if node.data == val:
                break
            prev_node = node
            node = node.next_node
        return prev_node, node

    def swap_nodes(self, val1: Any, val2: Any) -> None:
        """swap first instance of nodes with data values val1 and val2 respectively"""

        # no need to swap nodes of the contained data is equal
        if val1 == val2:
            return

        prev_node1, node1 = self._find_nodes_for_swp(val1)
        prev_node2, node2 = self._find_nodes_for_swp(val2)

        # raise exception if val1 or val2 were not found
        flag = None
        if node1 is None:
            flag = f"'{val1}' "
        if node2 is None:
            flag = f"'{val2}' " if flag is None else f"{flag}and '{val2}' "
        if flag is not None:
            flag += "not found in llist"
            raise ValueError(flag)
        assert node1 is not None and node2 is not None, "Uncaught exception; node None"

        # swap the pointers of the nodes before the nodes to be swapped
        if prev_node1 is None:
            self._head_node = node2
        else:
            prev_node1.next_node = node2
        if prev_node2 is None:
            self._head_node = node1
        else:
            prev_node2.next_node = node1

        # swap the pointers of the nodes
        node2_prev_next_node = node2.next_node
        node2.next_node = node1.next_node
        node1.next_node = node2_prev_next_node

    def nth_last_node(self, nth_node: int) -> Node:
        """find the nth last node in the list"""
        nth_last_pointer: Optional[Node] = None
        tail_pointer: Optional[Node] = self._head_node
        count = 0

        while tail_pointer is not None:
            if count >= nth_node:
                if nth_last_pointer is None:
                    nth_last_pointer = self._head_node
                else:
                    nth_last_pointer = nth_last_pointer.next_node
            tail_pointer = tail_pointer.next_node
            count += 1

        if nth_last_pointer is None:
            raise ValueError("nth_last_pointer None")

        return nth_last_pointer

    @property
    def middle_node(self) -> Optional[Node]:
        """find the center of the llist"""
        fast_pointer: Optional[Node] = self._head_node
        slow_pointer: Optional[Node] = self._head_node
        while fast_pointer is not None:
            fast_pointer = fast_pointer.next_node
            if fast_pointer is not None and slow_pointer is not None:
                fast_pointer = fast_pointer.next_node
                slow_pointer = slow_pointer.next_node
        return slow_pointer
