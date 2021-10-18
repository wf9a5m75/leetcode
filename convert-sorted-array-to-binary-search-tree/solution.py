import sys
from io import StringIO
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        sizeNums = len(nums)
        if (sizeNums == 0):
            return None
        right = sizeNums - 1
        mid = right >> 1
        root = TreeNode(nums[mid])

        if (0 <= mid - 1):
            root.left = self.sortedArrayToBST(nums[0 : mid])
        if (right >= mid + 1):
            root.right = self.sortedArrayToBST(nums[mid + 1 : right + 1])
        return root
