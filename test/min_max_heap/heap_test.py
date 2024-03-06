import unittest

from src.min_max_heap.heap import MinMaxHeap


class MinMaxHeapTest(unittest.TestCase):

    def test_initiallyEmptyHeap(self):
        heap = MinMaxHeap()
        heap.add(10)
        heap.add(15)
        heap.add(7)
        heap.add(2)
        heap.add(22)
        heap.add(100)
        heap.add(0)
        heap.add(1)

        self.assertEqual(0, heap.min())
        self.assertEqual(100, heap.max())


