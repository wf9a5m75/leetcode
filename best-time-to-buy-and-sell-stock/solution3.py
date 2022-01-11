class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #
        #  Greedy
        #    O(n) time
        #    O(1) space
        #
        buyPrice = prices[0]
        ans = 0
        for price in prices:
            profit = price - buyPrice
            ans = max(ans, profit)
            if profit < 0:
                buyPrice = price
        return ans
