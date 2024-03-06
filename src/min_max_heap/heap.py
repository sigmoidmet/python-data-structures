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
import sys


class MinMaxHeap:

    def __init__(self, array=None):
        self.__array = array if array is not None else []
        for i in range(len(self.__array) // 2 + 1, -1, -1):
            self.__pushDown(i)
        for i in range(1, len(self.__array)):
            self.__pushUp(i)

    def removeAt(self, index: int):
        if index == len(self.__array) - 1:
            self.__array.pop()
        else:
            self.__swap(index, len(self.__array) - 1)
            self.__pushDown(index)

    def __pushDown(self, i: int):
        if self.__isOnMinLevel(i):
            self.__pushDownMin(i)
        else:
            self.__pushDownMax(i)

    def __pushDownMin(self, i: int):
        if not self.__hasChildren(i):
            return
        smallestChildOrGrandChild = self.__findSmallestChildOrGrandChild(i)
        if self.__areParentAndChild(i, smallestChildOrGrandChild):
            if self.__array[smallestChildOrGrandChild] < self.__array[i]:
                self.__swap(i, smallestChildOrGrandChild)
        else:
            if self.__array[smallestChildOrGrandChild] < self.__array[i]:
                self.__swap(i, smallestChildOrGrandChild)
                smallestGrandchildParent = self.__parent(smallestChildOrGrandChild)
                if self.__array[smallestChildOrGrandChild] > self.__array[smallestGrandchildParent]:
                    self.__swap(smallestChildOrGrandChild, smallestGrandchildParent)
        self.__pushDown(smallestChildOrGrandChild)

    def __pushDownMax(self, i: int):
        if not self.__hasChildren(i):
            return
        smallestChildOrGrandChild = self.__findSmallestChildOrGrandChild(i)
        if self.__areParentAndChild(i, smallestChildOrGrandChild):
            if self.__array[smallestChildOrGrandChild] > self.__array[i]:
                self.__swap(smallestChildOrGrandChild, i)
        else:
            if self.__array[smallestChildOrGrandChild] > self.__array[i]:
                self.__swap(smallestChildOrGrandChild, i)
                smallestGrandChildParent = self.__parent(smallestChildOrGrandChild)
                if self.__array[smallestChildOrGrandChild] < self.__array[smallestGrandChildParent]:
                    self.__swap(smallestChildOrGrandChild, smallestGrandChildParent)
        self.__pushDown(smallestChildOrGrandChild)

    def __hasChildren(self, i):
        return self.__firstChild(i) < len(self.__array)

    def __findSmallestChildOrGrandChild(self, i):
        return min(self.__firstChild(i),
                   self.__secondChild(i),
                   self.__firstChild(self.__firstChild(i)),
                   self.__secondChild(self.__firstChild(i)),
                   self.__firstChild(self.__secondChild(i)),
                   self.__secondChild(self.__secondChild(i)),
                   key=lambda x: self.__array[x] if x < len(self.__array) else sys.maxsize)

    @staticmethod
    def __firstChild(i: int) -> int:
        return 2*i + 1

    @staticmethod
    def __secondChild(i: int):
        return 2*i + 2

    def __areParentAndChild(self, parent, child):
        return self.__parent(child) == parent

    def add(self, element: int):
        self.__array.append(element)
        self.__pushUp(len(self.__array) - 1)

    def __pushUp(self, i):
        if i == 0:
            return

        parent = self.__parent(i)
        if self.__isOnMinLevel(i):
            if self.__array[i] > self.__array[parent]:
                self.__swap(parent, i)
                self.__pushUpMax(parent)
            else:
                self.__pushUpMin(i)
        else:
            if self.__array[i] < self.__array[parent]:
                self.__swap(parent, i)
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
        if grandParent >= 0 and self.__array[i] > self.__array[grandParent]:
            self.__swap(grandParent, i)
            self.__pushUpMax(grandParent)

    def __pushUpMin(self, i: int):
        grandParent = self.__parent(self.__parent(i))
        if grandParent >= 0 and self.__array[i] < self.__array[grandParent]:
            self.__swap(grandParent, i)
            self.__pushUpMin(grandParent)

    @staticmethod
    def __parent(i: int) -> int:
        return (i + 1) // 2 - 1

    def __swap(self, i, smallestChildOrGrandChild):
        self.__array[smallestChildOrGrandChild], self.__array[i] = self.__array[i], self.__array[smallestChildOrGrandChild]

    def min(self):
        if not self.__array:
            raise AssertionError("Tried to call min on an empty min-max heap")
        return self.__array[0]

    def max(self):
        if not self.__array:
            raise AssertionError("Tried to call max on an empty min-max heap")
        if len(self.__array) == 1:
            return self.__array[0]
        if len(self.__array) == 2:
            return self.__array[1]
        return max(self.__array[1], self.__array[2])
