class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        if (N == 1):
            return 0

        farthest = 0
        ans = 0
        maxJump = 0

        for i in range(N):

            # The between from i to the farthest position,
            # we will find the next farthest jumpable position.
            maxJump = max(maxJump, i + nums[i])

            # We set the next farthest jumpable position
            # when we reach to the current farthest position.
            if farthest == i:
                farthest = maxJump

                ans += 1

                # If we can beyond the N - 1,
                # we can finish the process
                if (farthest >= N - 1):
                    break
        return ans
