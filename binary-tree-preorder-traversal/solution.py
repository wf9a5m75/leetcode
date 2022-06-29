# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if (root is None):
            return []
        stack = []
        
        results = []
        while(root is not None) or (len(stack) > 0):
            while(root is not None):
                # pre-order traversal
                results.append(root.val)
                
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            root = root.right
            
        return results
            
