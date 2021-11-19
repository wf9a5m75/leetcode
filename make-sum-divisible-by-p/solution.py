class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        N = len(nums)
        total = sum(nums)
        target = total % p
        if (target == 0):
            return 0

        mem = {0: -1}
        prefixSum = 0
        ans = N
        for i in range(N):
            prefixSum = (prefixSum + nums[i]) % p
            r = (prefixSum - target + p) % p

            if (r in mem):
                # debug
                # print(nums[mem[r] +1:i+1])

                ans = min(ans, i - mem[r])
            mem[prefixSum] = i

        return ans if ans < N else -1
