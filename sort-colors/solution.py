import random

class Solution:
    def quickSort(self, nums: List[int], start: int, end: int) -> None:
        if (start >= end):
            return
        L = start
        R = end
        pivot = nums[random.randint(L, R)]

        while(L <= R):
            while(L < end) and (nums[L] < pivot):
                L += 1
            while(R > start) and (nums[R] > pivot):
                R -= 1
            if (L > R):
                break
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R -= 1
        if (start < R):
            self.quickSort(nums, start, R)
        if (L < end):
            self.quickSort(nums, L, end)

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quickSort(nums, 0, len(nums) - 1)
