class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #
        # DP
        #   O(n) time
        #   O(n) space
        #
        N = len(prices)
        if (N <= 1):
            return 0

        wallet = [0] * N
        cost = [0] * N
        sell = [0] * N

        cost[0] = -prices[0] - fee
        sell[0] = 0
        # print(*wallet)
        # print(*cost)
        # print(*sell)
        for i in range(1, N):
            wallet[i] = max(wallet[i - 1], sell[i - 1])
            cost[i] = max(cost[i - 1], wallet[i] -prices[i] - fee)
            sell[i] =  prices[i] + cost[i]
            # print("-------")
            # print(*wallet)
            # print(*cost)
            # print(*sell)
        return max(wallet[-1], sell[-1])
