import unittest
import random

from src.skiplist.skiplist import SkipList


class SkipListTest(unittest.TestCase):

    def test_add(self):
        expectedResult = [3, 6, 7, 9, 12, 17, 19, 21, 25, 26]
        initialData = expectedResult.copy()
        random.shuffle(initialData)

        skipList = SkipList(3, 0.5)
        for key in initialData:
            skipList.add(key)

        self.assertListEqual(expectedResult, skipList.linearize())
