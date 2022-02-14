class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthestIdx = 0
        N = len(nums)
        i = 0
        while(i < N) and (i <= farthestIdx):
            farthestIdx = max(farthestIdx, i + nums[i])
            i += 1
        return farthestIdx >= N - 1   
