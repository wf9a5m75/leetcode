class Solution:

    # https://leetcode.com/problems/house-robber-ii/discuss/59921/9-lines-0ms-O(1)-Space-C%2B%2B-solution
    
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if (N == 0):
            return 0
        if (N == 1):
            return nums[0]

        return max(
            # We start from 0 to N - 2 (house(N - 1) is the neighbor of house(0))
            self.robber(nums, 0, N - 2),

            # We start from 1 to N - 1 (house(0) is the neighbor of house(N - 1))
            self.robber(nums, 1, N - 1)
        )
    def robber(self, nums: List[int], start: int, end: int) -> int:
        prePreHouse = 0
        current = 0
        for i in range(start, end + 1):
            num = nums[i]

            # (the amount at the i - 2) + num, or
            # we skip this house at i
            tmp = max(prePreHouse + num, current)

            prePreHouse = current
            current = tmp
        return current
