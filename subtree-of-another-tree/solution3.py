# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def matchSubTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (root == subRoot == None):
            return True
        if (root) and (subRoot) and (root.val == subRoot.val):
            return self.matchSubTree(root.left, subRoot.left) == self.matchSubTree(root.right, subRoot.right) == True
        else:
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (subRoot == None):
            return True
        if (root == None):
            return False

        queue = [root]
        while(queue):
            root = queue.pop(0)
            if root.val == subRoot.val:
                if (self.matchSubTree(root, subRoot)):
                    return True
            if (root.left):
                queue.append(root.left)
            if (root.right):
                queue.append(root.right)
        return False
