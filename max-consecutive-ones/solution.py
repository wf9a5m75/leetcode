class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOne = 0
        one = 0
        for num in nums:
            if num == 1:
                one += 1
            else:
                maxOne = max(maxOne, one)
                one = 0
        maxOne = max(maxOne, one)
        return maxOne
