# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        results = []
        currentLevel = [root]
        while(currentLevel):
            nextLevel = []
            values = []
            while(currentLevel):
                root = currentLevel.pop(0)
                values.append(root.val)
                if (root.left):
                    nextLevel.append(root.left)
                if (root.right):
                    nextLevel.append(root.right)
            results.append(values)

            currentLevel = nextLevel

        return results
