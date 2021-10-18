import sys
from io import StringIO
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        depth = 0
        maxDepth = 0

        while(root != None) or (len(stack) > 0):

            while(root != None):
                depth += 1
                stack.append((root, depth))
                root = root.left

            curr = stack.pop()
            root = curr[0]
            depth = curr[1]

            maxDepth = max(maxDepth, depth)

            root = root.right

        return maxDepth
