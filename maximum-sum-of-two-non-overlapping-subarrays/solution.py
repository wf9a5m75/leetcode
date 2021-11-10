class Solution:
    def generateAllWindows(self, nums: List[int], k: int) -> int:
        N = len(nums)

        results = []
        L = R = 0
        resultSum = 0
        while(R < k):
            resultSum += nums[R]
            R += 1
        results.append(resultSum)

        while(R < N):
            resultSum += nums[R] - nums[L]
            results.append(resultSum)
            R += 1
            L += 1

        return results

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        #
        # DP approach : O(N^2) time, O(N^2) space
        #

        first = self.generateAllWindows(nums, firstLen)
        second = self.generateAllWindows(nums, secondLen)

        N = len(first)
        M = len(second)
        dp = [[0] * (M + 1) for _ in range(N)]

        ans = 0
        for i, val1 in enumerate(first):

            dp[i][0] = val1

            for j, val2 in enumerate(second):

                if ((i <= j < i + firstLen) or (j <= i < j + secondLen)):
                    # overlapping
                    dp[i][j + 1] = dp[i][j]
                else:
                    dp[i][j + 1] = max(dp[i][j], val1 + val2)
                    ans = max(ans, dp[i][j + 1])

        return ans
