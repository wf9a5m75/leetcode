# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def postOrder(root):
            if root is None:
                return (0,0)

            # Collects the sums of left and right node,
            # then calculates the tilt
            left = postOrder(root.left)
            right = postOrder(root.right)
            tilt = abs(left[1] - right[1])

            # Sums up the answer
            tiltS = left[0] + right[0] + tilt

            return (tiltS, left[1] + right[1] + root.val)
        ans = postOrder(root)

        return ans[0]
