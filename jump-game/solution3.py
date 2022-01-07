class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)

        # We can jump to the nums[0] maximumly
        currJmp = nums[0]
        nextJmp = 0
        for i in range(N):
            nextJmp = max(nextJmp, i + nums[i])

            if i == currJmp:
                if nextJmp == currJmp:
                    return i == N - 1
                currJmp = nextJmp
        return True
