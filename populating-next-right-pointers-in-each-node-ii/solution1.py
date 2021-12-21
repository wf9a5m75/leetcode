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
        if root == None:
            return None
        queue = [root]
        while(queue):
            nextLevel = []
            while(queue):
                head = queue.pop(0)
                if (head.left):
                    nextLevel.append(head.left)
                if (head.right):
                    nextLevel.append(head.right)
                if (queue):
                    head.next = queue[0]
            queue = nextLevel
        return root
