from collections import Counter

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def preorder(root):
            if (root is None):
                return []

            results = [root.val]

            results += preorder(root.left)
            results += preorder(root.right)
            return results

        all_values = preorder(root)

        commons=Counter(all_values).most_common()
        results = []
        for common in commons:
            if common[1] == commons[0][1]:
                results.append(common[0])
        return results
