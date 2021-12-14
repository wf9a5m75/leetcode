# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        queue = [root]
        s = 0
        while(queue):
            root = queue.pop(0)

            # If root.val is in the range, sums it up
            if (low <= root.val <= high):
                s += root.val

            # If root.val is greater than low,
            # the left side of the root node might contain nodes
            if (low < root.val) and (root.left):
                queue.append(root.left)

            # If root.val is lower than high,
            # the right side of the root node might contain nodes
            if (root.val < high) and (root.right):
                queue.append(root.right)
        return s
