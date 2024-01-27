"""Nodes"""

from __future__ import annotations
from typing import Optional, Any
from dataclasses import dataclass
from functools import total_ordering


@dataclass
@total_ordering
class Node:
    """Node data structure"""

    data: Optional[Any] = None
    next_node: Optional[Any] = None

    def __str__(self) -> str:
        return str(self.data)

    def __eq__(self, other: Any) -> bool:
        if isinstance(self, Node) and isinstance(other, Node):
            return self.data == other.data
        return False

    def __lt__(self, other: Node) -> bool:
        if isinstance(self.data, int) and isinstance(other.data, int):
            return self.data < other.data
        raise TypeError


@dataclass
class DoublyLinkedNode(Node):
    """Doubly linked node data structure"""

    prev_node: Optional[Any] = None
