class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #
        # DP approach
        #
        N = len(prices)
        dpL = [0] * N
        dpR = dpL.copy()

        dpL[0] = prices[0]
        dpR[N - 1] = prices[N - 1]
        for i in range(1, N):
            dpL[i] = min(dpL[i - 1], prices[i])
            dpR[N - 1 - i] = max(dpR[N - i], prices[N - 1 - i])

        maxProfit = 0
        for i in range(N):
            maxProfit = max(maxProfit, dpR[i] - dpL[i])
        return maxProfit
