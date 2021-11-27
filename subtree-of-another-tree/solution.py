# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalTrees(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = [(root, subRoot)]
        while(queue):
            r, s = queue.pop(0)
            if (r == None) and (s == None):
                continue

            if (r == None) or (s == None):
                return False

            if (r.val != s.val):
                return False

            queue.append((r.left, s.left))
            queue.append((r.right, s.right))
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (root is None):
            return False
        if (subRoot is None):
            return True

        queue = [root]
        while(queue):
            root = queue.pop(0)
            if (root.val == subRoot.val):
                rc = self.equalTrees(root, subRoot)
                if (rc):
                    return True
            if (root.left):
                queue.append(root.left)
            if (root.right):
                queue.append(root.right)
        return False


    def another_isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        txt1 = str(root)
        txt2 = str(subRoot)
        return txt1.find(txt2) > -1
