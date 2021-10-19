class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)

        # xor = 0 ^ 1 ^ 2
        for val in range(n + 1):
            xor = xor ^ val

        # xor = 0 ^ 1
        for num in nums:
            xor = xor ^ num
        return xor
