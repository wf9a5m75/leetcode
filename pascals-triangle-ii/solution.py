import sys
from io import StringIO
from typing import Optional, List

class Solution:
    def __init__(self):
        self.mem = {
            0: 1,
            1: 1
        }
        self.maxFactor = 1
    def factorial(self, n):
        s = min(self.maxFactor, n)
        f = self.mem[s]
        s += 1
        for i in range(s, n + 1):
            f *= i
            self.mem[i] = f
        self.maxFactor = n
        return self.mem[n]

    def nCr(self, n, r):
        upper = self.factorial(n)
        lower = (self.factorial(r) * self.factorial(n - r))
        return upper // lower

    def getRow(self, rowIndex: int) -> List[int]:
        row = []
        for i in range(rowIndex + 1):
            row.append(self.nCr(rowIndex, i))
        return row

print(Solution().getRow(4))
