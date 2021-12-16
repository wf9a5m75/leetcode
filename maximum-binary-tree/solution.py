# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # https://leetcode.com/problems/maximum-binary-tree/discuss/106146/C++-O(N)-solution
        s = []
        for num in nums:
            cur = TreeNode(num)
            while(s) and (cur.val > s[-1].val):
                cur.left = s.pop()
            if (s):
                s[-1].right = cur

            s.append(cur)
        return s.pop(0)
