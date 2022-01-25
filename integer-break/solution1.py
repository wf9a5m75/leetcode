class Solution:
    def integerBreak(self, n: int) -> int:
        if (n == 3):
            return 2
        if (n == 2):
            return 1

        @cache
        def dp(rest: int)->int:
            if rest == 0:
                return 1

            p = 0
            for i in range(1, rest + 1):
                p = max(p, i * dp(rest - i))
            return p
        return dp(n)
