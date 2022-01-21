class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        kinds = Counter(nums)
        N = max(nums)
        dp = [0, 0]
        sIdx = 0
        for i in range(1, N + 1):
            nIdx = (sIdx + 1) % 2
            dp[sIdx] = max(dp[sIdx] + kinds.get(i, 0) * i, dp[nIdx])
            sIdx = nIdx
        return max(dp)
