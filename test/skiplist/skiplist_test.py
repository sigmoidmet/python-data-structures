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

    def test_get(self):
        expectedResult = [3, 6, 7, 9, 12, 17, 19, 21, 25, 26]
        initialData = expectedResult.copy()
        random.shuffle(initialData)

        skipList = SkipList(3, 0.5)
        for key in initialData:
            skipList.add(key)

        self.assertEqual(19, skipList.get(19))

    def test_get_whenNotExist_shouldReturnNone(self):
        expectedResult = [3, 6, 7, 9, 12, 17, 19, 21, 25, 26]
        initialData = expectedResult.copy()
        random.shuffle(initialData)

        skipList = SkipList(3, 0.5)
        for key in initialData:
            skipList.add(key)

        skipList.delete(19)

        self.assertIsNone(skipList.get(19))
        self.assertIsNone(skipList.get(500))
