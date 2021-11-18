from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mem = defaultdict(int)

        # The sum of an empty subarray is zero
        mem[0] = 1

        s = ans = 0
        for num in nums:
            s += num

            # If "s - k" exists in the mem,
            # the sum from somewhere before to this index is k.
            if (s - k) in mem:
                ans += mem[s - k]

            mem[s] += 1

        return ans
