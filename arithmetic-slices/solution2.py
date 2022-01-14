class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        nums.append(float("inf"))
        N = len(nums)
        ans = 0
        cnt = 0
        prevDiff = float("inf")
        for i in range(1, N):
            diff = nums[i] - nums[i - 1]
            if diff == prevDiff:
                cnt += 1
            else:
                ans += (cnt * (cnt + 1)) >> 1
                cnt = 0
            prevDiff = diff
        return ans
