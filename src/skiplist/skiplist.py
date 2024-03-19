import random
from typing import Optional

from src.skiplist.node import Node


class SkipList:

    def __init__(self, maxLevel: int, fractionOfLevelReferencingNextLevel: float):
        self.maxLevel = maxLevel
        self.fractionOfLevelReferencingNextLevel = fractionOfLevelReferencingNextLevel
        self.head = Node(-1, self.maxLevel)
        self.level = 0

    def add(self, key):
        forUpdate = [None] * (self.maxLevel + 1)
        item = self.__tryFind(key, forUpdate)

        if item is None or item.key != key:
            randomLevel = self.__chooseLevel(forUpdate)
            node = Node(key, randomLevel)
            self.__rearrangeReferencesAfterInsert(forUpdate, node)

    def __chooseLevel(self, forUpdate):
        randomLevel = self.__randomLevel()

        if randomLevel > self.level:
            for i in range(self.level + 1, randomLevel + 1):
                forUpdate[i] = self.head
            self.level = randomLevel

        return randomLevel

    def __randomLevel(self) -> int:
        lvl = 0
        while random.random() < self.fractionOfLevelReferencingNextLevel and lvl < self.maxLevel:
            lvl += 1
        return lvl

    @staticmethod
    def __rearrangeReferencesAfterInsert(forUpdate: [Node], node: Node):
        for i in range(len(node.forward)):
            node.forward[i] = forUpdate[i].forward[i]
            forUpdate[i].forward[i] = node

    def get(self, key):
        item = self.__tryFind(key)

        return item.key if item and item.key == key else None

    def delete(self, key):
        forUpdate = [None] * (self.maxLevel + 1)
        item = self.__tryFind(key, forUpdate)

        if item is None or item.key != key:
            return

        self.__rearrangeReferencesAfterDelete(forUpdate, item)
        self.__fixLevel()

    def __tryFind(self, key, forUpdate=None) -> Optional[Node]:
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            if forUpdate:
                forUpdate[i] = current

        return current.firstLevel()

    def __rearrangeReferencesAfterDelete(self, forUpdate: [Node], item: Node):
        for i in range(self.level + 1):
            if forUpdate[i].forward[i] != item:
                break
            forUpdate[i].forward[i] = item.forward[i]

    def __fixLevel(self):
        while self.level > 0 and self.head.forward[self.level] is None:
            self.level -= 1

    def linearize(self) -> [int]:
        result = []
        node = self.head.firstLevel()
        while node is not None:
            result.append(node.key)
            node = node.forward[0]
        return result
