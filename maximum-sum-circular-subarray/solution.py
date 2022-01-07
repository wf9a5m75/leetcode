class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        biggest = nums[0]
        minSum = maxSum = total = 0
        smallest = 300000

        for num in nums:
            total += num
            maxSum = max(maxSum + num, num)
            biggest = max(biggest, maxSum)

            minSum = min(minSum + num, num)
            smallest = min(smallest, minSum)

        if (biggest > 0):
            return max(biggest, total - smallest)
        else:
            return biggest
