from collections import Counter
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        #
        # O(N) time, O(N) space
        #
        ans = 0
        mem = Counter(nums)
        for num in nums:
            if (num + k) in mem:
                ans += mem[num + k]
        return ans

    def countKDifference_O_N2(self, nums: List[int], k: int) -> int:
        #
        # O(N ** 2) time, O(1) space
        #
        ans = 0
        N = len(nums)
        for i in range(N - 1):
            for j in range(i, N):
                if (abs(nums[i] - nums[j]) == k):
                    ans += 1
        return ans
        
