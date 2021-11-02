# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        while(queue):
            nextLevel = []
            s = 0
            while(queue):
                root = queue.pop(0)
                s += root.val
                if (root.left):
                    nextLevel.append(root.left)
                if (root.right):
                    nextLevel.append(root.right)

            if (nextLevel):
                queue = nextLevel
            else:
                return s
