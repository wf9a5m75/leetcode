class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        #
        # Greedy approach
        #   O(n) time
        #   O(1) space
        #

        N = len(values)
        largestIdx = 0
        ans = 0
        for i in range(1, N):
            ans = max(ans, values[largestIdx] + values[i] + largestIdx - i)

            if values[largestIdx] + largestIdx - i < values[i]:
                largestIdx = i

        return ans
