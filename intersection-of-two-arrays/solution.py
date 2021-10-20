class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dp = [False] * 1000
        for i in nums1:
            dp[i] = True

        results = []
        for j in nums2:
            if dp[j]:
                dp[j] = False
                results.append(j)
        return results

    def intersection_simple(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))
