class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*N for _ in range(N)]
        for i in range(N):
            dp[i][i]=True
        ans = s[0]
        for j in range(N):
            for i in range(j):
                #
                #     a b c d c b e
                #    ├───────────────
                #  a │T
                #  b │  T
                #  c │    T
                #  d │      T
                #  c │    T   T    ←  cdc
                #  b │  T       T  ← b   b
                #  e │            T
                #
                if s[i]==s[j] and (dp[i+1][j-1] or j==i+1):
                    dp[i][j]=True
                    if j-i+1>len(ans):
                        ans=s[i:j+1]
        return ans
