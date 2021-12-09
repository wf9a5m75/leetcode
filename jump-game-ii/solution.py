class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        if (N <= 1):
            return 0

        # We can jump from 0 to nums[0] + 1
        L, R = 0, nums[0]

        # At least one jump to beyond the last index,
        # because N >= 2
        times = 1

        # Continues jumping until we are able to jump beyond the last index
        while(R < N - 1):
            times += 1

            # Since nums[i] denotes the length of maximum from i,
            # we are able to reach to the last index if the R beyonds the last index.
            # Thus, we just need to find the farthest position from each i position.
            farthestR = 0
            for i in range(L, R + 1):
                farthestR = max(farthestR, i + nums[i])

            # We are able to continue jumping
            # from the current R to the farthestR on next time,
            # because we can jump up to the current R on this time.
            L = R
            R = farthestR

        return times
            
