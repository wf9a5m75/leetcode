# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def postorderTraversal_slow(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def postOrder(root):
            if root:
                postOrder(root.left)
                postOrder(root.right)
                result.append(root.val)

        postOrder(root)
        return result

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        result = []
        stack = []
        while root or stack:

            while root:
                result.insert(0, root.val)
                stack.append(root)
                root = root.right

            root = stack.pop()
            root = root.left

        return result
