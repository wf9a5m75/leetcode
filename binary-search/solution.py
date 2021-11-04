class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums)
        while(L != R):
            mid = (L + R) >> 1
            if (nums[mid] < target):
                L = mid + 1
            else:
                R = mid
        if (L >= len(nums)) or (nums[L] != target):
            return -1
        return L
