class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        NEGATIVE_INF = -2**31-1
        maxVals = [NEGATIVE_INF, NEGATIVE_INF, NEGATIVE_INF]

        for num in nums:
            if num in maxVals:
                continue

            if maxVals[0] < num:
                maxVals.insert(0, num)
                maxVals.pop()
            elif maxVals[1] < num:
                maxVals.insert(1, num)
                maxVals.pop()
            elif maxVals[2] < num:
                maxVals.insert(2, num)
                maxVals.pop()

        if (maxVals[2] != NEGATIVE_INF):
            return maxVals[2]
        else:
            return maxVals[0]
