class Solution:
    def countPrimes(self, n: int) -> int:
        if (n < 3):
            return 0
        if (n == 3):
            # 2
            return 1
        if (n == 4):
            # 2,3
            return 2
        dp = [True] * n
        ans = 0
        dp[0] = dp[1] = False

        ans = 2
        for i in range(4, n):
            if (i % 2 == 0) or (i % 3 == 0) or (dp[i] == False):
                dp[i] == False
                continue

            ans += 1
            j = i * 2
            while(j < n):
                if (j< n):
                    dp[j] = False
                j += i

        return ans

            
