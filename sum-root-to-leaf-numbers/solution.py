# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0

        queue = [(root, 0)]
        s = 0
        while(queue):
            nextLevel = []
            while(queue):
                root, pathSum = queue.pop()
                if root.left == root.right == None:
                    s += pathSum * 10 + root.val
                else:
                    pathSum = pathSum * 10 + root.val
                    if root.left:
                        nextLevel.append((root.left, pathSum))
                    if root.right:
                        nextLevel.append((root.right, pathSum))
            queue = nextLevel
        return s
