# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        results = []

        def dfs(root, path = []):
            # just in case
            if root == None:
                return path

            path.append(str(root.val))
            if root.left == root.right == None:
                results.append("->".join(path))
                path.pop()
                return
            if root.left:
                dfs(root.left, path)
            if root.right:
                dfs(root.right, path)
            path.pop()
        dfs(root)
        return results
            
