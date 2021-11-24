class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        ans = []
        for i in range(N):
            L, R = i + 1, N - 1

            if (i > 0) and (nums[i] == nums[i - 1]):
                continue

            while(L < R):
                s = nums[i] + nums[L] + nums[R]
                if (s == 0):
                    ans.append([nums[i], nums[L], nums[R]])
                    L += 1
                    while(nums[L - 1] == nums[L]) and (L < R):
                        L += 1

                elif (s > 0):
                    R -= 1
                else:
                    L += 1
        return ans
