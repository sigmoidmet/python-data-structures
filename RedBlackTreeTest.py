import random
import unittest

from RedBlackTree import RedBlackTree, TreeNode, Color


class RedBlackTreeTest(unittest.TestCase):

    def test_linearize(self):
        tree = RedBlackTree()
        tree.root = TreeNode(2, Color.BLACK, None,
                             TreeNode(1, Color.RED, None),
                             TreeNode(3, Color.BLACK, None, right=TreeNode(4, Color.RED, None)))

        self.assertListEqual([i for i in range(1, 5)], tree.linearize())

    def test_insert(self):
        array = [x for x in range(1000)]
        sortedArray = array.copy()
        random.shuffle(array)
        inputArray = array

        tree = RedBlackTree()

        for x in inputArray:
            tree.insert(x)

        self.assertListEqual(sortedArray, tree.linearize())

    def test_get(self):
        array = [x for x in range(1000)]
        random.shuffle(array)
        inputArray = array

        tree = RedBlackTree()

        for x in inputArray:
            tree.insert(x)

        self.assertEquals(1, tree.get(1))
        self.assertEquals(2, tree.get(2))
        self.assertEquals(369, tree.get(369))
        self.assertEquals(500, tree.get(500))
        self.assertEquals(256, tree.get(256))
        self.assertEquals(978, tree.get(978))
        self.assertEquals(999, tree.get(999))

        self.assertIsNone(tree.get(1259))

    def test_delete(self):
        array = [x for x in range(1000)]
        sortedArray = array.copy()
        random.shuffle(array)
        start = random.randint(0, 999)
        forDeletionArray = array[start: random.randint(start, 1000)]
        inputArray = array

        tree = RedBlackTree()

        for x in inputArray:
            tree.insert(x)

        for x in forDeletionArray:
            tree.delete(x)
            sortedArray.remove(x)

        self.assertListEqual(sortedArray, tree.linearize())
