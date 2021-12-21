"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        queue = [root]
        while(queue):
            nextQ = []
            while(queue):
                root = queue.pop(0)
                if (queue):
                    root.next = queue[0]
                if root == None:
                    continue

                if root.left:
                    nextQ.append(root.left)
                if root.right:
                    nextQ.append(root.right)
            queue = nextQ
        return head
