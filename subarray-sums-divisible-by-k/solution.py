from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mem = defaultdict(int)

        s = ans = 0

        # The sum from index(0) to index(i) becomes zero
        mem[0] = 1

        for num in nums:
            s += num
            rest = s % k
            if rest in mem:
                ans += mem[rest]
            mem[rest] += 1
        return ans
