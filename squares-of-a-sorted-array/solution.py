import sys
from io import StringIO
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queueL = [root.left]
        queueR = [root.right]

        while(len(queueL) > 0) and (len(queueR) > 0):
            currL = queueL.pop(0)
            currR = queueR.pop(0)
            if (currL == currR == None):
                continue
            if (currL == None) or (currR == None):
                return False
            if (currL.val != currR.val):
                return False
            queueL.append(currL.left)
            queueR.append(currR.right)

            queueL.append(currL.right)
            queueR.append(currR.left)
        return len(queueL) == len(queueR)
