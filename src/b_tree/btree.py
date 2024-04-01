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
    pass
