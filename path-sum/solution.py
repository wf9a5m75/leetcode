import sys
from io import StringIO
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack = []
        while(root) or (len(stack)):
            while(root):
                stack.append((root, targetSum - root.val))
                targetSum -= root.val
                root = root.left

            curr = stack.pop()
            root = curr[0]
            if (curr[1] == 0) and (root.left == root.right == None):
                return True
            root = curr[0].right
            targetSum = curr[1]
        return False



    def hasPathSum_slow(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        def dfs(root, rest):
            rest = rest - root.val

            # Only True if rest == 0 at a leaf
            if (root.left == root.right == None):
                return (rest == 0)

            # If we are not at a leaf, just continue
            if (root.left) and (dfs(root.left, rest)):
                return True
            if (root.right) and (dfs(root.right, rest)):
                return True
            return False

        return dfs(root, targetSum)
