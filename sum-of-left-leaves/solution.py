# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def traverse(root: TreeNode, isLeft: bool) -> int:
            s = 0
            if (isLeft) and (root.left == root.right == None):
                s = root.val
            else:
                if (root.left):
                    s += traverse(root.left, True)
                if (root.right):
                    s += traverse(root.right, False)
            return s

        return traverse(root, False)
