# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        N = len(preorder)
        root = TreeNode(preorder[0])
        s = [root]
        for i in range(1, N):
            if (s) and (preorder[i] < s[-1].val):
                s[-1].left = TreeNode(preorder[i])
                s.append(s[-1].left)
            else:
                last = s.pop()
                while(s) and (preorder[i] > s[-1].val):
                    last = s.pop()
                last.right = TreeNode(preorder[i])
                s.append(last.right)
        return root
