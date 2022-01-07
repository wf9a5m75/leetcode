class Solution:
    def maxSubArray(self, A: List[int]) -> int:
        # DP
        sizeA = len(A)
        dp = [ A[0] ] * (sizeA + 1)
        for i in range(1, sizeA):
            dp[i] = max(dp[i - 1] + A[i], A[i])
        return max(dp)
