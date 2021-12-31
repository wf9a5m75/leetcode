# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        #
        # DFS using queue
        #    keeping minimum value, maxmum value, and node
        #
        # Time complexity : O(N)
        #    We traverse all node once.
        #
        # Space complexity : O(N)
        #    Maximum queue size is O(N)
        #
        queue = deque()

        # Starts from root
        queue.append((root.val, root.val, root))

        ans = 0
        while(queue):
            minVal, maxVal, node = queue.popleft()

            # Updates the minimum and maxium values
            if node.val < minVal:
                ans = max(ans, maxVal - node.val)
                minVal = node.val
            elif maxVal < node.val:
                ans = max(ans, node.val - minVal)
                maxVal = node.val

            # Adds next nodes
            if (node.left):
                queue.append((minVal, maxVal, node.left))

            if (node.right):
                queue.append((minVal, maxVal, node.right))
        return ans
