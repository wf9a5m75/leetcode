class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        lenNums1, lenNums2 = len(nums1), len(nums2)

        @cache
        def dp(i: int, j: int) -> int:
            if (i == lenNums1) or (j == lenNums2):
                return 0

            matchCnt2 = 0
            if (nums1[i] == nums2[j]):
                matchCnt2 = 1 + dp(i + 1, j + 1)
            else:
                matchCnt2 = dp(i + 1, j + 1)


            return matchCnt2
        return dp(0, 0)

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        lenNums1, lenNums2 = len(nums1), len(nums2)

        dp = [[0] * (lenNums2 + 1) for _ in range(lenNums1 + 1)]

        ans = 0
        for i in range(lenNums1 - 1, -1, -1):
            for j in range(lenNums2 - 1, -1, -1):
                if (nums1[i] == nums2[j]):
                    dp[i][j] = dp[i + 1][j + 1] + 1
                    ans = max(ans, dp[i][j])

        return ans
        
