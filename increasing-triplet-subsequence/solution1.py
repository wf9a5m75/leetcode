class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        #
        # DP + binary search (ref: longest-increasing-subsequence)
        #   O(N log N) times
        #   O(N) spaces
        #
        dp = [nums[0]]
        for num in nums:
            if (dp[-1] < num):
                dp.append(num)
            else:
                L, R = 0, len(dp) - 1
                while(L != R):
                    mid = (L + R) >> 1
                    if (dp[mid] < num):
                        L = mid + 1
                    else:
                        R = mid
                dp[L] = num
            if len(dp) == 3:
                return True
        return False
