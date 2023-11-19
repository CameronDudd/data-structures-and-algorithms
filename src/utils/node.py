"""Nodes"""

from typing import Optional, Any
from dataclasses import dataclass


@dataclass
class Node:
    """Node data structure"""

    data: Optional[Any] = None
    next_node: Optional[Any] = None

    def __str__(self) -> str:
        return f"{self.data} > "


@dataclass
class DoublyLinkedNode(Node):
    """Doubly linked node data structure"""

    prev_node: Optional[Any] = None

    def __str__(self) -> str:
        return " < " + super().__str__()
