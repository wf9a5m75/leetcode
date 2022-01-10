class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minSub = maxSub = 1
        ans = nums[0]
        for num in nums:
            if num < 0:
                # (minSub could be a negative value) * (negative value) = (could be a positive value)
                # (maxSub could be a positive value) * (negative value) = (could be a negative value)
                maxSub, minSub = max(num, minSub * num), min(num, maxSub * num)
            else:
                # (minSub could be a negative value) * (positive value) = (could be a positive value)
                # (maxSub could be a positive value) * (positive value) = (could be a negative value)
                maxSub, minSub = max(num, maxSub * num), min(num, minSub * num)
            ans = max(ans, maxSub)
        return ans
