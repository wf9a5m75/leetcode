class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        L = R = 0
        N = len(nums)
        hasZero = False
        ans = 0
        while(R < N):
            if (nums[R] == 1):
                R += 1
            elif (hasZero == False):
                hasZero = True
                R += 1
            else:
                ans = max(ans, R - L - 1)
                if (nums[L] == 0):
                    hasZero = False
                L += 1
        ans = max(ans, R - L - 1)
        return ans
            
