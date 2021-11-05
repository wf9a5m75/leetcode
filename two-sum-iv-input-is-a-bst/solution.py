# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if (root is None):
            return False

        mem = set()
        queue = []
        head = root
        while(head or queue):
            while(head):
                rest = k - head.val
                # if (rest == head.val):
                #     mem.add(head.val)
                #     head = head.left
                #     continue
                if (rest in mem):
                    return True
                mem.add(head.val)

                if (head.right):
                    queue.append(head.right)
                head = head.left
            if (queue):
                head = queue.pop()
            else:
                break
        return False
