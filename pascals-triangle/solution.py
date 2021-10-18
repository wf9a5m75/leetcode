import sys
from io import StringIO
from typing import Optional, List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        results = [[1], [1, 1]]

        for i in range(3, numRows + 1):
            dp = results[-1]

            row = []
            prev = 0
            for j in range(i - 1):
                row.append(prev + dp[j])
                prev = dp[j]

            row.append(1)
            results.append(row)

        return results[:numRows]


"""
            1
          1  1
        1  2  1
      1  3  3  1
    1  4  6  4  1
  1  5  10 10 5 1
1  6  15 20  15  6  1
"""

for row in Solution().generate(6):
    print(*row)
