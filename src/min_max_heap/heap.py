# A min-max heap is a complete binary tree containing alternating min (or even) and max (or odd) levels.
# Even levels are for example 0, 2, 4, etc., and odd levels are respectively 1, 3, 5, etc.
# We assume in the next points that the root element is at the first level, i.e., 0.
#
# Each node in a min-max heap has a data member (usually called key)
# whose value is used to determine the order of the node in the min-max heap.
#
# The root element is the smallest element in the min-max heap.
#
# One of the two elements in the second level which is a max (or odd) level, is the greatest element in the min-max heap
#
# Let x be any node in a min-max heap.
#   If x is on a min (or even) level, then x.key is the minimum key among all keys in the subtree with root x.
#   If x is on a max (or odd) level, then x.key is the maximum key among all keys in the subtree with root x.
#
# A node on a min (max) level is called a min (max) node.
#
# A max-min heap is defined analogously;
# in such a heap, the maximum value is stored at the root, and the smallest value is stored at one of its children
import math


class MinMaxHeap:

    def __init__(self, array=None):
        self.array = array if array is not None else []

    def add(self, element: int):
        self.array.append(element)
        self.__pushUp(len(self.array) - 1)

    def __pushUp(self, i):
        if i == 0:
            return

        parent = self.__parent(i)
        if self.__isOnMinLevel(i):
            if self.array[i] > self.array[parent]:
                self.array[i], self.array[parent] = self.array[parent], self.array[i]
                self.__pushUpMax(parent)
            else:
                self.__pushUpMin(i)
        else:
            if self.array[i] < self.array[parent]:
                self.array[i], self.array[parent] = self.array[parent], self.array[i]
                self.__pushUpMin(parent)
            else:
                self.__pushUpMax(i)

    @staticmethod
    def __isOnMinLevel(i: int) -> int:
        if i == 0:
            return True
        return int(math.log2(i + 1)) % 2 == 0

    def __pushUpMax(self, i: int):
        grandParent = self.__parent(self.__parent(i))
        if grandParent >= 0 and self.array[i] > self.array[grandParent]:
            self.array[i], self.array[grandParent] = self.array[grandParent], self.array[i]
            self.__pushUpMax(grandParent)

    def __pushUpMin(self, i: int):
        grandParent = self.__parent(self.__parent(i))
        if grandParent >= 0 and self.array[i] < self.array[grandParent]:
            self.array[i], self.array[grandParent] = self.array[grandParent], self.array[i]
            self.__pushUpMin(grandParent)

    @staticmethod
    def __parent(i: int) -> int:
        return (i + 1) // 2 - 1

    def min(self):
        if not self.array:
            raise AssertionError("Tried to call min on an empty min-max heap")
        return self.array[0]

    def max(self):
        if not self.array:
            raise AssertionError("Tried to call max on an empty min-max heap")
        if len(self.array) == 1:
            return self.array[0]
        if len(self.array) == 2:
            return self.array[1]
        return max(self.array[1], self.array[2])

    def remove(self, element: int):
        pass
