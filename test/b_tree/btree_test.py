import random
import unittest

from src.b_tree.btree import BTree


class BTreeTest(unittest.TestCase):

    def test_get(self):
        array = [x for x in range(1000)]
        random.shuffle(array)
        inputArray = array

        tree = BTree(4)

        for x in inputArray:
            tree.insert(x)

        self.assertEqual(1, tree.get(1))
        self.assertEqual(2, tree.get(2))
        self.assertEqual(369, tree.get(369))
        self.assertEqual(500, tree.get(500))
        self.assertEqual(256, tree.get(256))
        self.assertEqual(978, tree.get(978))
        self.assertEqual(999, tree.get(999))

        self.assertIsNone(tree.get(1259))
