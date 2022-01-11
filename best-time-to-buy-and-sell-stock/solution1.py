class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        #
        # One pass approach
        #
        minPrice = 99999999
        maxProfit = 0
        for price in prices:
            if (price < minPrice):
                minPrice = price
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice
        return maxProfit
