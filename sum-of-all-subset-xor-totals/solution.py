class Solution:
    def subsetXORSum(self, nums: List[int], xorSoFar = 0) -> int:
        if (len(nums) == 0):
            return xorSoFar

        nextNums = nums[1:]

        # Does not include nums[0]
        result = self.subsetXORSum(nextNums, xorSoFar)

        # Including nums[0]
        result += self.subsetXORSum(nextNums, xorSoFar ^ nums[0])

        return result
