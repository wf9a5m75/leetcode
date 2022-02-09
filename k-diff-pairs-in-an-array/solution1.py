class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        valuePos = {}
        N = len(nums)
        for i in range(N):
            val = nums[i]
            valuePos[val] = i
        ans = 0
        for i in range(N):
            val = nums[i]
            if val not in valuePos:
                continue

            if (val + k) in valuePos:
                ans += 1 if valuePos[val + k] > i else 0
            if (k != 0) and ((val - k) in valuePos):
                ans += 1 if valuePos[val - k] > i else 0

            del valuePos[val]
        return ans
