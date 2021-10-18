import sys
from io import StringIO
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_Slow:
    def preorderTraversal(self, root):
        if root is None:
            return [None]
        queue = [root]
        result = []
        while(len(queue) > 0):
            root = queue.pop(0)
            if root is None:
                result.append(None)
                continue
            else:
                result.append(root.val)
            queue.append(root.left)
            queue.append(root.right)
        return result

    def isSameTree_slow(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pValues = self.preorderTraversal(p)
        qValues = self.preorderTraversal(q)

        return pValues == qValues
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queueL = [p]
        queueR = [q]

        while(len(queueL) > 0) and (len(queueR) > 0):
            p = queueL.pop(0)
            q = queueR.pop(0)
            if (p == q == None):
                continue
            if (p == None) or (q == None):
                return False
            if (p.val != q.val):
                return False

            queueL.append(p.left)
            queueR.append(q.left)

            queueL.append(p.right)
            queueR.append(q.right)

        return len(queueL) == len(queueR)
