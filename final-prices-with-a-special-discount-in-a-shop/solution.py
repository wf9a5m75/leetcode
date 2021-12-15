class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s = []
        result = []
        N = len(prices)

        for i in range(N - 1, -1, -1):
            discount = 0
            while(s) and (s[-1] > prices[i]):
                s.pop()
            if (s):
                discount = s[-1]
            result.insert(0, prices[i] - discount)

            s.append(prices[i])
        return result
