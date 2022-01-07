class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        #
        # Similar question: https://leetcode.com/problems/house-robber/
        #

        if (len(nums) == 1):
            return nums[0]
        counts = Counter(nums)

        kinds = sorted(counts)

        N = len(kinds)
        if (N == 1):
            return nums[0] * kinds[0]

        start, end = kinds[0], kinds[N -1]
        dp = [0] * (end - start + 1)
        dp[0] = kinds[0] * counts[kinds[0]]
        if (kinds[0] + 1) in counts:
            dp[1] = max(dp[0], kinds[1] * counts[kinds[1]])
        else:
            dp[1] = dp[0]

        j = 2
        for i in range(start + 2, end + 1):
            dp[j] = max(dp[j - 1], dp[j - 2] + i * counts.get(i, 0))
            j += 1
        return dp[-1]
