from typing import Optional

from src.red_black_tree.color import Color


class TreeNode:

    def __init__(self,
                 key,
                 color: Color,
                 parent: Optional['TreeNode'] = None,
                 left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None):
        self.color = color
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return f"{self.key} - {self.color}"