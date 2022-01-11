class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        i = 0
        N = len(prices)
        while(i < N - 1):
            # Calculate the profit between (i) and (i + 1)
            profit = prices[i + 1] - prices[i]
            # If total increases, we add the profit.
            # We assume we sell the stock.
            #
            # Otherwise, we keep the stock
            ans = max(ans, ans + profit)
            i += 1
        return ans
