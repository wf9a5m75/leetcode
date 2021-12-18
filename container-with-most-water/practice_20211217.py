class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Find the highest height
        maxH = max(height)

        # Since we only need the dimension between L and R,
        # we approach using the L,R two pointers
        L, R = 0, len(height) - 1

        ans = 0
        while(L != R):

            # If answer (maximum water so far) beyonds the possible maximum water with current L and R,
            # there is no possibility.
            # So, break the process
            if maxH * (R - L) <= ans:
                break

            water = min(height[L], height[R]) * (R - L)

            # Keep the maximum water
            ans = max(ans, water)



            # if height[L] is smaller than height[R],
            # we try to find more higher height on left side
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return ans
        
