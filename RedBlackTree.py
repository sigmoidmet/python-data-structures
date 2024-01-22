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

    def __init__(self,
                 key,
                 color: Color,
                 parent: Optional['TreeNode'] = None,
                 left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None):
        self.color = color
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return f"{self.key} - {self.color}"


class RedBlackTree:

    def __init__(self):
        self.root = None

    def insert(self, key):
        toInsert = TreeNode(key, Color.RED)

        lastNodeBeforeInsert = None
        currentNode = self.root

        while currentNode is not None:
            lastNodeBeforeInsert = currentNode
            if key < currentNode.key:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        toInsert.parent = lastNodeBeforeInsert

        if lastNodeBeforeInsert is None:
            self.root = toInsert
        elif key < lastNodeBeforeInsert.key:
            lastNodeBeforeInsert.left = toInsert
        else:
            lastNodeBeforeInsert.right = toInsert

        self.__insertFixup(toInsert)

    def __insertFixup(self, node: TreeNode):
        while node != self.root and node.parent.color == Color.RED:
            if node.parent.parent.left == node.parent:
                uncle = node.parent.parent.right
                if self.__isRed(uncle):
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.__rotateLeft(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self.__rotateRight(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if self.__isRed(uncle):
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.__rotateRight(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self.__rotateLeft(node.parent.parent)

        self.root.color = Color.BLACK

    @staticmethod
    def __isRed(node: TreeNode):
        return node is not None and node.color == Color.RED

    def __rotateLeft(self, x: TreeNode):
        y = x.right

        if y is None:
            return

        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def __rotateRight(self, y: TreeNode):
        x = y.left

        if x is None:
            return

        y.left = x.right
        if x.right is not None:
            x.right.parent = y

        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        x.right = y
        y.parent = x

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
