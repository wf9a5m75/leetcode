class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #
        # DP approach : O(N * N)
        #
        ans = -2**31

        currS = set()
        for num in nums:

            nextS = set()

            # A subarray starts from current index
            nextS.add(num)
            ans = max(ans, num)

            # Another subarraies have been started from previous indicies.
            for prev in currS:
                p = prev * num
                ans = max(ans, p)
                nextS.add(p)

            currS = nextS
        return ans
