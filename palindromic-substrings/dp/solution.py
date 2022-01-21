class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)

        # All characters are palindromic substrings
        ans = len(s)

        dp = [[False] * N for _ in range(N)]
        for y in range(N):
            dp[y][y] = True
            for x in range(y):
                if s[y] == s[x]:
                    dp[y][x] = dp[y - 1][x + 1] or (x + 1 == y)
                    if dp[y][x]:
                        ans += 1
            # print(dp[y])
        return ans
