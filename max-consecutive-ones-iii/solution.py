class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        N = len(nums)
        L = R = 0
        ans = 0
        while(R < N):
            while(R < N) and ((nums[R] == 1) or (k > 0)):
                if (nums[R] == 0):
                    k -= 1
                R += 1
            if (R == N):
                break

            # print(k, nums[L:R])
            ans = max(ans, R - L)

            while(nums[L] == 1):
                L += 1
            # print(k, nums[L:R])

            if (k == 0):
                k += 1
                L += 1
            # print(k, nums[L:R])

        ans = max(ans, N - L)
        # print(nums[L:N])
        return ans
