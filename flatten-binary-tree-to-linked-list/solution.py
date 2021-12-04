# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        head = TreeNode(0)
        stack = []
        while(stack or root):
            while(root):
                if (root.right):
                    stack.append(root.right)
                rootL = root.left

                root.left = None
                root.right = None

                head.right = root
                head = head.right

                root = rootL

            if stack:
                root = stack.pop()
