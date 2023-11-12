"""llist module"""

from __future__ import annotations
from typing import Any, Optional, Tuple


class Node:
    """Node data structure"""

    # pylint: disable=too-few-public-methods

    def __init__(self, data: Any = None, link: Optional[Node] = None) -> None:
        self.data = data
        self.link = link

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    """Linked List data structure"""

    def __init__(self, data: Any = None, link: Optional[Node] = None) -> None:
        self._head_node: Node = Node(data=data, link=link)

    def __iter__(self) -> LinkedList:
        return LinkedList(data=self._head_node.data, link=self._head_node.link)

    def __next__(self) -> Node:
        if self._head_node is None:
            raise StopIteration
        current_head_node = self._head_node
        current_link = current_head_node.link
        self._head_node = current_link if current_link is not None else Node()
        return current_head_node

    def __str__(self) -> str:
        list_str = "<"
        current_node: Optional[Node] = self._head_node
        while current_node is not None:
            if current_node.data is not None:
                list_str += str(current_node.data)
            current_link = current_node.link
            if current_link is not None:
                list_str += ", "
            current_node = current_link
        list_str += ">"
        return list_str

    @property
    def head(self) -> Optional[Node]:
        """get head node"""
        return self._head_node

    def remove_node(self, value: Any) -> None:
        """remove first node in list with matching value"""
        current_node = self._head_node
        if current_node.data == value:
            if current_node.link is None:
                raise ValueError("Cannot remove Node, would destroy llist by setting head to None")
            self._head_node = current_node.link
        else:
            searching = True
            while searching:
                next_node = current_node.link

                # handle case of value not in llist
                if next_node is None:
                    searching = False
                    raise ValueError(f"LList does not contain Node with data {value}")

                if next_node.data == value:
                    current_node.link = next_node.link
                    searching = False
                else:
                    current_node = next_node

    def append_left(self, new_value: Any) -> None:
        """add node to start of llist"""
        new_node = Node(data=new_value, link=self._head_node)
        self._head_node = new_node

    def append_right(self, value: Any) -> None:
        """add node to end of llist"""
        new_node = Node(data=value, link=None)
        current_node = self._head_node
        while current_node.link is not None:
            current_node = current_node.link
        current_node.link = new_node

    def _find_nodes_for_swp(self, val: Any) -> Tuple[Optional[Node], Optional[Node]]:
        """find a node containing val and return said node with preceeding node"""
        node: Optional[Node] = self._head_node
        prev_node = None
        # find node
        while node is not None:
            if node.data == val:
                break
            prev_node = node
            node = node.link
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
            prev_node1.link = node2
        if prev_node2 is None:
            self._head_node = node1
        else:
            prev_node2.link = node1

        # swap the pointers of the nodes
        node2_prev_link = node2.link
        node2.link = node1.link
        node1.link = node2_prev_link

    def nth_last_node(self, n: int) -> Node:
        """find the nth last node in the list"""
        nth_last_pointer: Optional[Node] = None
        tail_pointer: Optional[Node] = self._head_node
        count = 0

        while tail_pointer is not None:
            if count >= n:
                if nth_last_pointer is None:
                    nth_last_pointer = self._head_node
                else:
                    nth_last_pointer = nth_last_pointer.link
            tail_pointer = tail_pointer.link
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
            fast_pointer = fast_pointer.link
            if fast_pointer is not None and slow_pointer is not None:
                fast_pointer = fast_pointer.link
                slow_pointer = slow_pointer.link
        return slow_pointer
