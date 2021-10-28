class Solution:

    # https://leetcode.com/problems/trapping-rain-water/solution/
    def trap(self, height: List[int]) -> int:
        if (len(height) == 0):
            return 0

        result = 0
        N = len(height)
        dpLeftMax = [0] * N
        dpRightMax = [0] * N

        dpLeftMax[0] = height[0]
        for i in range(1, N):
            dpLeftMax[i] = max(height[i], dpLeftMax[i - 1])

        dpRightMax[N - 1] = height[N - 1]
        for i in range(N - 2, -1, -1):
            dpRightMax[i] = max(height[i], dpRightMax[i + 1])

        for i in range(1, N - 1):
            result += min(dpLeftMax[i], dpRightMax[i]) - height[i]
        return result
