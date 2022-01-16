class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1 :
            return 1

        two = three = five = 0
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            dp[i] = min(dp[two] * 2, dp[three] * 3, dp[five] * 5)
            if dp[i] == dp[two] * 2:
                two += 1
            if dp[i] == dp[three] * 3:
                three += 1
            if dp[i] == dp[five] * 5:
                five += 1
        return dp[n - 1]

            
