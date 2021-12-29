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
            nextLevel = []
            leftNode = None
            while(queue):
                root = queue.pop(0)
                if (leftNode):
                    leftNode.next = root
                leftNode = root
                if root:
                    nextLevel.append(root.left)
                    nextLevel.append(root.right)
            queue = nextLevel

        return head
