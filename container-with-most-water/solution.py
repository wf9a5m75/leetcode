class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1

        # To determine the maximum value at each range,
        # find the highest value before moving.
        highest = max(height)

        # answer
        maxWater = 0
        while(L != R):

            # Calculate the containable water
            water = min(height[L], height[R]) * (R - L)
            # print(L, height[L:R+1], R, " = ", water)

            # Compair with the maximum so far.
            maxWater = max(maxWater, water)

            # If the maxWater is grater than
            # the maximum containable water at this range,
            # it means there is no greater containable water range than current.
            if (maxWater >= highest * (R - L)):
                break

            # Move pointer of lower side
            if (height[L] < height[R]):
                L += 1
            else:
                R -= 1
        return maxWater
