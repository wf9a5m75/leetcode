"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if (root == None):
            return []

        results = []
        q = [root]
        while(q):
            currLevel = []
            nextQ = []
            while(q):
                curr = q.pop(0)
                currLevel.append(curr.val)

                nextQ += curr.children
            results.append(currLevel)
            q = nextQ
        return results
