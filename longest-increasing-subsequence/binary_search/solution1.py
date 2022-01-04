class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]
        ans = 1
        N = len(nums)
        for i in range(1, N):
            if dp[ans - 1] < nums[i]:
                dp.append(nums[i])
                ans += 1
            else:
                L, R = 0, ans - 1
                while(L != R):
                    mid = (L + R) >> 1
                    if nums[i] <= dp[mid]:
                        R = mid
                    else:
                        L = mid + 1
                dp[L] = nums[i]
        return ans
