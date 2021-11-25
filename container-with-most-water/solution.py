class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        maxWater = 0
        while(L != R):
            water = min(height[L], height[R]) * (R - L)
            maxWater = max(maxWater, water)
            if (height[L] < height[R]):
                L += 1
            else:
                R -= 1
        return maxWater


#     def maxArea2(self, height: List[int]) -> int:
#         N = len(height)
#         dpL = [0] * N
#         dpR = [0] * N

#         prevL = 0
#         prevR = N - 1
#         for i in range(N):
#             if height[prevL] < height[i]:
#                 dpL[i] = i
#                 prevL = i
#             else:
#                 dpL[i] = prevL

#             if height[prevR] < height[N - 1 - i]:
#                 dpR[N - 1 - i] = N - 1 - i
#                 prevR = N - 1 - i
#             else:
#                 dpR[N - 1 - i] = prevR


#         # print(dpL)
#         # print(dpR)
#         ans = 0
#         for i in range(N):
#             ans = max(ans, min(height[dpL[i]], height[dpR[i]]) * (dpR[i] - dpL[i]))

#             ans = max(ans, min(height[i], height[N - 1]) * (N - 1 - i))

#             ans = max(ans, min(height[i], height[0]) * i)

#         return ans
