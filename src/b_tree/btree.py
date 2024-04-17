from src.b_tree.node import Node


# Properties of B-Tree:
# 1. All leaves are at the same level.
# 2. B-Tree is defined by the term minimum degree ‘t'. The value of ‘t' depends upon disk block size.
# 3. Every node except the root must contain at least t-1 keys. The root may contain a minimum of 1 key.
# 4. All nodes (including root) may contain at most (2*t – 1) keys.
# 5. The number of node's children is equal to the number of keys in it plus 1.
# 6. All keys of a node are sorted in increasing order.
#    The child between k1 and k2 contains all keys in the range from k1 and k2.
# 7. B-Tree grows and shrinks from the root which is unlike Binary Search Tree.
# 8. Like other balanced Binary Search Trees, the time complexity to search, insert, and delete is O(log n).
# 9. Insertion of a node in B-Tree happens only at Leaf Node.


class BTree:

    def __init__(self, termMinimumDegree):
        self.root = Node(True)
        self.termMinimumDegree = termMinimumDegree

    def insert(self, key):
        root = self.root

        if self.__hasTooManyKeys(root):
            node = Node()
            self.root = node
            node.child.insert(0, root)
            self.__splitChild(node, 0)
            self.__insertToNode(node, key)
        else:
            self.__insertToNode(root, key)

    def __hasTooManyKeys(self, node: Node) -> bool:
        return len(node.keys) == self.__maxKeys()

    def __splitChild(self, node: Node, childIndex):
        child = node.child[childIndex]
        splitChildSecondPart = Node(child.isLeaf)
        node.child.insert(childIndex + 1, splitChildSecondPart)
        node.keys.insert(childIndex, child.keys[self.termMinimumDegree - 1])
        splitChildSecondPart.keys = child.keys[self.termMinimumDegree: self.__maxKeys()]
        child.keys = child.keys[0: self.termMinimumDegree - 1]
        if not child.isLeaf:
            splitChildSecondPart.child = child.child[self.termMinimumDegree: 2 * self.termMinimumDegree]
            child.child = child.child[0: self.termMinimumDegree - 1]

    def __maxKeys(self) -> int:
        return (2 * self.termMinimumDegree) - 1

    def __insertToNode(self, node: Node, key):
        indexToInsert = len(node.keys) - 1
        if node.isLeaf:
            node.keys.append((None, None))
            while indexToInsert >= 0 and key < node.keys[indexToInsert]:
                node.keys[indexToInsert + 1] = node.keys[indexToInsert]
                indexToInsert -= 1
            node.keys[indexToInsert + 1] = key
        else:
            while indexToInsert >= 0 and key < node.keys[indexToInsert]:
                indexToInsert -= 1
            indexToInsert += 1
            if len(node.child[indexToInsert].keys) == self.__maxKeys():
                self.__splitChild(node, indexToInsert)
                if key > node.keys[indexToInsert]:
                    indexToInsert += 1
            self.__insertToNode(node.child[indexToInsert], key)

