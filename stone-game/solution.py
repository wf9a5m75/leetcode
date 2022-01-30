class Solution:
    def stoneGame_backtrack(self, piles: List[int]) -> bool:
        N = len(piles)
        @cache
        def dp(L: int, R: int) -> int:
            if (L == R):
                return 0
            #nextTurn = (aliceTurn + 1) % 2
            aliceTurn = (R - L - N)  % 2 == 1

            if aliceTurn:
                return max(piles[L] + dp(L + 1, R), piles[R] + dp(L, R - 1))
            else:
                return min(-piles[L] + dp(L + 1, R), -piles[R] + dp(L, R - 1))
        return dp(0, N - 1) > 0

    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        for L in range(N - 2, -1, -1):
            for R in range(N - 1, 0, -1):

                aliceTurn = (R - L - N) % 2 == 1
                if aliceTurn:
                    dp[L][R] = max(piles[L] + dp[L + 1][R], piles[R] + dp[L][R - 1])
                else:
                    dp[L][R] = min(-piles[L] + dp[L + 1][R], -piles[R] + dp[L][R - 1])
        return dp[0][N - 1] > 0
