import random

from src.skiplist.node import Node


class SkipList:

    def __init__(self, maxLevel: int, fractionOfLevelReferencingNextLevel: float):
        self.maxLevel = maxLevel
        self.fractionOfLevelReferencingNextLevel = fractionOfLevelReferencingNextLevel
        self.head = Node(-1, self.maxLevel)
        self.level = 0

    def add(self, key):
        forUpdate = [None] * (self.maxLevel + 1)
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            forUpdate[i] = current

        current = current.firstLevel()
        if current is None or current.key != key:
            randomLevel = self.chooseLevel(forUpdate)
            node = Node(key, randomLevel)
            self.rearrangeReferences(forUpdate, node)

    def chooseLevel(self, forUpdate):
        randomLevel = self.randomLevel()

        if randomLevel > self.level:
            for i in range(self.level + 1, randomLevel + 1):
                forUpdate[i] = self.head
            self.level = randomLevel

        return randomLevel

    def randomLevel(self) -> int:
        lvl = 0
        while random.random() < self.fractionOfLevelReferencingNextLevel and lvl < self.maxLevel:
            lvl += 1
        return lvl

    @staticmethod
    def rearrangeReferences(forUpdate: [Node], node: Node):
        for i in range(len(node.forward)):
            node.forward[i] = forUpdate[i].forward[i]
            forUpdate[i].forward[i] = node

    def get(self, key):
        current = self.head
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]

        current = current.forward[0]

        return current.key if current and current.key == key else None


    def delete(self, key):
        pass

    def linearize(self) -> [int]:
        result = []
        node = self.head.firstLevel()
        while node is not None:
            result.append(node.key)
            node = node.forward[0]
        return result
