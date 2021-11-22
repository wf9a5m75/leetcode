class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        L, R = 0, N - 1
        while(L != R):
            mid = (L + R) >> 1
            if (nums[mid] > nums[mid + 1]):
                R = mid
            else:
                L = mid + 1
        return L
