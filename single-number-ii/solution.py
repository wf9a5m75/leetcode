class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
            0
            0
            0
            1
            1
            1
        110 0011
        ---------
        110 0014
        %3
        ---------
        110 0011
        """

        ans = 0
        N = len(nums)
        for i in range(31, -1, -1):
            cnt = 0
            mask = 1 << i
            for num in nums:
                cnt += 1 if (num & mask) > 0 else 0

            if (cnt % 3 == 1):
                ans = mask | ans

        if (ans & 0x80000000) > 0:
            ans = -(2 **32 - ans)
        return ans
