class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        mask = 1
        for i in range(32):
            oneCnt = 0
            for num in nums:
                if (num & mask) != 0:
                    oneCnt += 1
            zeroCnt = (N - oneCnt)
            ans += oneCnt * zeroCnt
            mask <<= 1
        return ans
