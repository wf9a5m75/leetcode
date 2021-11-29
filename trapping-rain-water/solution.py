class Solution:
    #
    # (1) Brute forth approach
    #
    def trap(self, height: List[int]) -> int:
        N = len(height)
        ans = 0
        for i in range(N):
            maxL = maxR = height[i]
            # Find highest on left side
            for j in range(i - 1, -1, -1):
                maxL = max(maxL, height[j])

            # Find highest on right side
            for j in range(i + 1, N):
                maxR = max(maxR, height[j])

            ans += min(maxL, maxR) - height[i]
        return ans

    #
    # (2) DP approach
    #
    def trap(self, height: List[int]) -> int:
        N = len(height)
        maxL = [0] * N
        maxR = maxL.copy()

        # Build two DP tables
        i = 1
        maxL[0], maxR[N - 1] = height[0], height[N - 1]
        while(i < N):
            maxL[i] = max(maxL[i - 1], height[i])
            maxR[N - 1 - i] = max(maxR[N - i], height[N - 1 - i])
            i += 1

        # Calculate water on each location
        ans = 0
        for i in range(N):
            ans += min(maxL[i], maxR[i]) - height[i]
        return ans

    #
    # (3) Monotonic Stack approach
    #
    def trap(self, height: List[int]) -> int:
        ans = 0
        N = len(height)
        stack = []
        for i in range(N):
            while(stack) and (height[i] > height[stack[-1]]):
                j = stack.pop()
                if len(stack) == 0:
                    break
                distance = i - stack[-1] - 1
                ans += (min(height[i], height[stack[-1]]) - height[j]) * distance
            stack.append(i)
        return ans

    #
    # (4) Two pointers approach
    #
    def trap(self, height: List[int]) -> int:
        ans = 0
        N = len(height)
        L, R = 0, N - 1
        maxL = maxR = 0
        while(L != R):
            if (height[L] < height[R]):
                if (height[L] > maxL):
                    maxL = height[L]
                else:
                    ans += maxL - height[L]
                L += 1
            else:
                if (height[R] > maxR):
                    maxR = height[R]
                else:
                    ans += maxR - height[R]
                R -= 1
        return ans
