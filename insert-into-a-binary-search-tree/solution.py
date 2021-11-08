# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if (root is None):
            return TreeNode(val)
        if (root.val < val):
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root

    def insertIntoBST_BFS(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if (root is None):
            return TreeNode(val)
        head = root
        queue = [root]
        while(queue):
            root = queue.pop(0)
            if (val < root.val):
                if (root.left is None):
                    root.left = TreeNode(val)
                    return head
                else:
                    queue.append(root.left)
            else:
                if (root.right is None):
                    root.right = TreeNode(val)
                    return head
                else:
                    queue.append(root.right)
