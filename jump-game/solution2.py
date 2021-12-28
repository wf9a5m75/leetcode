class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        current = 0

        for i in range(N):

            # Pick up the maximum jumping distance either
            #   1) current - 1
            #      or
            #   2) pick up the nums[i]
            current = max(current - 1, nums[i])

            # If i + current beyonds the N - 1,
            # we can jump to N - 1.
            # Because the jump step denotes the maximum number of jumping.
            if (i + current >= N - 1):
                return True

            # If i + current == i, we can't move anymore.
            if (i + current == i):
                return False

        # We can't find the satisfied condition.
        return False
