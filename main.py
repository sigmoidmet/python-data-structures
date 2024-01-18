from enum import Enum
from typing import Optional


# Properties of Red Black Tree:
# 1. Each node is either red or black
# 2. The root is always black
# 3. Each leaf(None) is always black
# 4. If a node is red, then both its children are black
# 5. All "simple" paths from each node to leaves contain the same number of black nodes
#
# Definitions:
# Black height - number of black nodes from node X (not included) to a leaf


class Color(Enum):
    RED = 1
    BLACK = 2


class TreeNode:

    def __init__(self, key, color: Color, p, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.color = color
        self.key = key
        self.left = left
        self.right = right
        self.p = p


class RedBlackTree:

    def __init__(self):
        self.root = None

    def linearize(self) -> list:
        if self.root is None:
            return []

        stack = [self.root]
        linear_view = []

        while len(stack) > 0:
            element = stack.pop()
            if isinstance(element, TreeNode):
                if element.right is not None:
                    stack.append(element.right)
                if element.left is not None:
                    stack.append(element.key)
                    stack.append(element.left)
                else:
                    linear_view.append(element.key)
            else:
                linear_view.append(element)

        return linear_view
