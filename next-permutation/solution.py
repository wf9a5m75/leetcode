class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        i = N - 2
        while(i >= 0) and (nums[i] >= nums[i + 1]):
            i -= 1

        if (i >= 0):
            j = i + 1
            while(j < N) and (nums[i] < nums[j]):
                j += 1
            nums[i], nums[j - 1] = nums[j - 1], nums[i]
            L = i + 1
        else:
            L = 0
        R = N - 1


        while(L < R):
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R -= 1
