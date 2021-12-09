class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        N = len(heights)
        maxArea = 0
        for i in range(N):
            while(stack) and (heights[i] < heights[stack[-1]]):
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                area = h * w
                maxArea = max(maxArea, area)
            stack.append(i)
        return maxArea
