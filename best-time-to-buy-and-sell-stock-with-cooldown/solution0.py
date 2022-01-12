class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if N <= 1:
            return 0
        s0 = [0] * N
        s1 = [0] * N
        s2 = [0] * N

        s1[0] = -prices[0]  # We buy a stcok at prices[0], so the profit is -prices[0]
        s2[0] = -float("inf")
        # print(s0)
        # print(s1)
        # print(s2)
        # print("--------")
        for i in range(1, N):
            s0[i] = max(s0[i - 1], s2[i - 1])
            s1[i] = max(s1[i - 1], s0[i - 1] - prices[i])
            s2[i] = s1[i - 1] + prices[i]
            # print(s0)
            # print(s1)
            # print(s2)
            # print("--------")
        return max(s0[N - 1], s2[N - 1])
