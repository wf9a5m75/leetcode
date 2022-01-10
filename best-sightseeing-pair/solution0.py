class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        #
        # Monotonic stack approach
        #   O(n) time
        #   O(n) space
        #

        N = len(values)
        s = deque()
        i = N - 1
        ans = 0
        while(i >= 0):
            while(s) and (values[s[-1]] < values[i]):
                ans = max(ans, values[s[-1]] + values[i] + i - s[-1])
                s.pop()
            if (s):
                ans = max(ans, values[s[-1]] + values[i] + i - s[-1])
            s.append(i)
            i -= 1
        return ans
