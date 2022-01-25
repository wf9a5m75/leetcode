class Solution:

    def combinationSum4(self, nums: List[int], target: int) -> int:
        #
        # Explanation
        # https://leetcode.com/problems/combination-sum-iv/discuss/85036/1ms-Java-DP-Solution-with-Detailed-Explanation
        #
        @cache
        def dp(rest: int) -> int:
            if (rest == 0):
                return 1

            total = 0
            for num in nums:
                if rest - num >= 0:
                    total += dp(rest - num)
            return total
        return dp(target)
