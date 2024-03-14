class Node:

    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)

    def firstLevel(self):
        return self.forward[0]

    def __str__(self):
        return f"{self.key}, {self.forward}"

