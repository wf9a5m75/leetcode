class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i, val in enumerate(nums):
            rightSum = total - val - leftSum
            if leftSum == rightSum:
                return i
            leftSum += val
        return -1
