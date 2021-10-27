# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if (root is None):
            return [0]

        results = []
        currentLevel = [root]
        while(currentLevel):
            currentSum = 0
            currentN = len(currentLevel)
            nextLevel = []
            while(currentLevel):
                root = currentLevel.pop(0)
                currentSum += root.val
                if (root.left):
                    nextLevel.append(root.left)
                if (root.right):
                    nextLevel.append(root.right)
            results.append(currentSum / currentN)

            currentLevel = nextLevel

        return results
