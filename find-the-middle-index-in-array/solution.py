class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i, num in enumerate(nums):
            rightSum = total - num - leftSum
            # print("i={}, leftSum = {}, rightSum = {}".format(i, leftSum, rightSum))
            if (rightSum == leftSum):
                return i
            leftSum += num

        return -1
