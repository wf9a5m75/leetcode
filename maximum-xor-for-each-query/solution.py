class Solution:
    def getMaximumXor_optimized(self, nums: List[int], maximumBit: int) -> List[int]:
        mask = 2**maximumBit - 1

        N = len(nums)
        ans = [0] * N
        prefixXOR = 0
        j = N - 1
        for num in nums:
            prefixXOR = prefixXOR ^ num
            ans[j] = prefixXOR ^ mask
            j -= 1

        return ans

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mask = 2**maximumBit - 1

        prefixXOR = 0
        for num in nums:
            prefixXOR = prefixXOR ^ num

        ans = []
        for num in reversed(nums):
            ans.append( prefixXOR ^ mask )
            prefixXOR = prefixXOR ^ num
        return ans
            
