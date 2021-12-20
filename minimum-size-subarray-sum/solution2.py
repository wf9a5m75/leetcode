class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        s = 0
        N = len(nums)
        ans = N + 1
        for R, num in enumerate(nums):
            s += num
            if s >= target:
                # print(s, R - L, nums[L:R+1])

                # The summation of the range(L to R) beyonds the target
                ans = min(ans, R - L + 1)

                # Move L until s < target
                while(s >= target):
                    s -= nums[L]
                    L += 1

                # The new summation of the range (L - 1 to R) also beyonds the target
                ans = min(ans, R - L + 2)
        # If not found, return 0
        if ans == N + 1:
            return 0
        return ans
