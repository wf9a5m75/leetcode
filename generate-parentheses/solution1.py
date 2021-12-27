class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [
            [""],
            ["()"],
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]
        def helper(n):
            if (len(dp[n]) > 0):
                return dp[n]

            results = []
            for i in range(n):
                for left in helper(i):
                    for right in helper(n - i - 1):
                        results.append("({}){}".format(left, right))
            dp[n] = results
            return dp[n]

        helper(n)
        return dp[n]
    
