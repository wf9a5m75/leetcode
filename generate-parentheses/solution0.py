class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [
            ["()"]
        ]
        def fibo(n):
            if len(dp) >= n:
                return dp[n - 1]

            ans = set()
            for seq in fibo(n - 1):
                for i in range(len(seq)):
                    ans.add(seq[:i] + "()" + seq[i:])

            ans = list(ans)
            dp.append(ans)
            return ans

        return fibo(n)
