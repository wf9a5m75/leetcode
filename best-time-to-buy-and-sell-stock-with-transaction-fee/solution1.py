class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #
        # Greedy
        #   O(n) time
        #   O(1) space
        #
        N = len(prices)
        if (N <= 1):
            return 0
        ans = 0
        lowest = prices[0]
        for i in range(1, N):
            if lowest > prices[i]:
                lowest = prices[i]
            elif lowest + fee < prices[i]:
                ans += prices[i] - fee - lowest
                lowest = prices[i] - fee
        return ans
