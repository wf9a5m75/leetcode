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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        top = root
        queue = deque()
        if root:
            queue.append(root)
        while(queue):
            nextQ = deque()
            while(queue):
                cur = queue.popleft()
                if len(queue) > 0:
                    cur.next = queue[0]

                if (cur.left):
                    nextQ.append(cur.left)
                if (cur.right):
                    nextQ.append(cur.right)
            queue = nextQ
        return top
