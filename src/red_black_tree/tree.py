from typing import Optional

from src.red_black_tree.color import Color
from src.red_black_tree.node import TreeNode


# Properties of Red Black Tree:
# 1. Each node is either red or black
# 2. The root is always black
# 3. Each leaf(None) is always black
# 4. If a node is red, then both its children are black
# 5. All "simple" paths from each node to leaves contain the same number of black nodes
#
# Definitions:
# Black height - number of black nodes from node X (not included) to a leaf

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

    def delete(self, key: int):
        node = self.__get(key)
        self.deleteNode(node)

    def get(self, key: int) -> Optional[int]:
        node = self.__get(key)
        return node.key if node is not None else None

    def __get(self, key: int) -> Optional[TreeNode]:
        if self.root is None:
            return None

        node = self.root

        while node is not None and node.key != key:
            if node.key > key:
                node = node.left
            else:
                node = node.right

        return node

    def deleteNode(self, node: TreeNode):
        if node is None:
            return

        replacingNode = node
        replacingNodeOriginalColor = replacingNode.color

        if node.left is None:
            nodeWithPotentialRedBlackTreeViolations = node.right
            self.__transplant(node, node.right)
        elif node.right is None:
            nodeWithPotentialRedBlackTreeViolations = node.left
            self.__transplant(node, node.left)
        else:
            replacingNode = self.__minimum(node.right)
            replacingNodeOriginalColor = replacingNode.color
            nodeWithPotentialRedBlackTreeViolations = replacingNode.right
            if replacingNode.parent == node:
                if nodeWithPotentialRedBlackTreeViolations is not None:
                    nodeWithPotentialRedBlackTreeViolations.parent = replacingNode
            else:
                self.__transplant(replacingNode, replacingNode.right)
                replacingNode.right = node.right
                replacingNode.right.parent = replacingNode
            self.__transplant(node, replacingNode)
            replacingNode.left = node.left
            replacingNode.left.parent = replacingNode
            replacingNode.color = node.color
        if replacingNodeOriginalColor == Color.BLACK:
            self.__deleteFixup(nodeWithPotentialRedBlackTreeViolations)

    def __transplant(self, higherNode: TreeNode, lowerNode: TreeNode):
        if higherNode.parent is None:
            self.root = lowerNode
        elif higherNode == higherNode.parent.left:
            higherNode.parent.left = lowerNode
        else:
            higherNode.parent.right = lowerNode

        if lowerNode is not None:
            lowerNode.parent = higherNode.parent

    @staticmethod
    def __minimum(node: TreeNode) -> TreeNode:
        while node.left is not None:
            node = node.left
        return node

    def __deleteFixup(self, x: TreeNode):
        if x is None:
            return

        while x != self.root and x.color == Color.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if self.__isRed(w):
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.__rotateLeft(x.parent)
                    w = x.parent.right
                if self.__isBlack(w.left) and self.__isBlack(w.right):
                    w.color = Color.RED
                    x = x.parent
                elif self.__isBlack(w.right):
                    w.left.color = Color.BLACK
                    w.color = Color.RED
                    self.__rotateRight(w)
                    w = x.parent.right
                w.color = x.parent.color
                x.parent.color = Color.BLACK
                w.right.color = Color.BLACK
                self.__rotateLeft(x.parent)
            else:
                w = x.parent.left
                if self.__isRed(w):
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.__rotateRight(x.parent)
                    w = x.parent.left
                if self.__isBlack(w.left) and self.__isBlack(w.right):
                    w.color = Color.RED
                    x = x.parent
                elif self.__isBlack(w.left):
                    w.right.color = Color.BLACK
                    w.color = Color.RED
                    self.__rotateLeft(w)
                    w = x.parent.left
                w.color = x.parent.color
                x.parent.color = Color.BLACK
                w.left.color = Color.BLACK
                self.__rotateRight(x.parent)

            x = self.root

        x.color = Color.BLACK

    @staticmethod
    def __isRed(node: TreeNode):
        return node is not None and node.color == Color.RED

    @staticmethod
    def __isBlack(node: TreeNode):
        return node is None or node.color == Color.BLACK

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
