import sys
from io import StringIO
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if root == None:
                return depth

            depthL = depthR = depth
            if root.left:
                depthL = dfs(root.left, depth + 1)

            if root.right:
                depthR = dfs(root.right, depth + 1)
            else:
                depthR = depthL

            if root.left == None:
                depthL = depthR

            return min(depthL, depthR)
        if root == None:
            return 0

        return dfs(root, 1)
