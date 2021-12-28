class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if (N == 1):
            return nums[0]
        if (N == 2):
            return max(nums[0], nums[1])

        # We try two robbing cases,
        #   1) we start from 0 to N - 2,
        #     or
        #   2) we start from 1 to N - 1.
        #
        return max(self.robbing(nums, 0, N - 2),
                self.robbing(nums, 1, N - 1))

    def robbing(self, nums: List[int], start: int, end: int) -> int:
        preHouse = 0
        current = 0
        for i in range(start, end + 1):
            beforeCurrent = current
            current = max(current, preHouse + nums[i])
            preHouse = beforeCurrent
        return current
