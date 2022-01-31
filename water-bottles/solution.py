class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        #
        # O(logN)
        #
        total = numBottles
        emptyBottles = 0
        while(numBottles > 0):
            currentBottles = numBottles + emptyBottles

            numBottles = int(currentBottles / numExchange)
            total += numBottles

            emptyBottles = currentBottles % numExchange

        return total

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # https://leetcode.com/problems/water-bottles/discuss/743148/JavaPython-3-O(logN)-and-O(1)-codes-w-brief-explanation-and-analysis.
        return numBottles + (numBottles - 1) // (numExchange - 1)
