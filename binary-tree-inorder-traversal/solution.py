import sys
from io import StringIO
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = []
        result = []
        while(root is not None) or (len(stack) > 0):
            while(root is not None):
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root.val)
            root = root.right

        return result
