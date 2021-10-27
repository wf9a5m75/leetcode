# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], leftMin = -2**31 -1, rightMax = 2**31) -> bool:
        if (root == None):
            return True
        isSelfValid = leftMin < root.val < rightMax
        isLeftValid = self.isValidBST(root.left, leftMin, root.val)
        isRightValid = self.isValidBST(root.right, root.val, rightMax)

        # print(root.val, isSelfValid, isLeftValid, isRightValid)
        return (isSelfValid == isLeftValid == isRightValid)
