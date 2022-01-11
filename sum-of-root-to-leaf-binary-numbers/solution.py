# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((root, 0))
        ans = 0
        while(queue):
            root, soFar = queue.popleft()
            if root.left == root.right == None:
                # print("{:b}".format((soFar << 1) + root.val))
                ans += (soFar << 1) + root.val
            else:
                soFar = (soFar << 1) + root.val
                if (root.left):
                    queue.append((root.left, soFar))
                if (root.right):
                    queue.append((root.right, soFar))
        return ans
