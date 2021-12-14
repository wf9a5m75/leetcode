class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        DP (Optimized little)
            time complecity: O(N * half)
            space complecity: O(N * half)
        """
        total = sum(nums)
        if total & 1 == 1:
            return False

        half = int(total / 2)
        N = len(nums)

        currS = set()
        currS.add(0)
        # Try all numbers one by one
        for i, num in enumerate(nums):
            nextS = set()
            for m in currS:
                nextS.add(m)

                if m + num <= half:
                    nextS.add(m + num)
            currS = nextS

        return half in currS
