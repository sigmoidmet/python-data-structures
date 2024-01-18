import unittest

from RedBlackTree import RedBlackTree, TreeNode, Color


class RedBlackTreeTest(unittest.TestCase):

    def test_linearize(self):
        tree = RedBlackTree()
        tree.root = TreeNode(2, Color.BLACK, None,
                             TreeNode(1, Color.RED, None),
                             TreeNode(3, Color.BLACK, None, right=TreeNode(4, Color.RED, None)))

        self.assertListEqual([i for i in range(1, 5)], tree.linearize())
