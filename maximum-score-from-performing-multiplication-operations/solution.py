class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        N = len(nums)
        M = len(multipliers)

        # Due to the memory limit, @cache is not good.
        # @lru_cache expands up to 2000, but @cache expands to unlimited.
        @lru_cache(2000)
        def backtrack(i: int, left: int) -> int:
            if i == M:
                return 0

            multi = multipliers[i]
            right = N - 1 - (i - left)
            return max(multi * nums[left] + backtrack(i + 1, left + 1),
                      multi * nums[right] + backtrack(i + 1, left))
        return backtrack(0, 0)
