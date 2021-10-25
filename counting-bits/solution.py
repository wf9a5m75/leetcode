
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 = 0
        # 1 = dp[1 // 2] + (1 % 2) = dp[0] + 1 = 1
        # 2 = dp[2 // 2] + (2 % 2) = dp[1] + 0 = 1
        # 3 = dp[3 // 2] + (3 % 2) = dp[2] + 1 = 2
        # 4 = dp[4 // 2] + (4 % 2) = dp[2] + 0 = 1
        # 5 = dp[5 // 2] + (5 % 2) = dp[2] + 1 = 2
        # 6 = dp[6 // 2] + (6 % 2) = dp[3] + 0 = 2
        # 7 = dp[7 // 2] + (7 % 2) = dp[3] + 1 = 3
        # 8 = dp[8 // 2] + (8 % 2) = dp[4] + 0 = 1
        dp = [0]
        for i in range(1, n + 1):
            dp.append(dp[i // 2] + (i % 2))
        return dp
