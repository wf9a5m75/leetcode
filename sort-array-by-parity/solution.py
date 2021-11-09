class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        N = len(nums)
        L = 0
        R = N - 1
        while(L < R):
            while(L < R) and (nums[L] & 1 == 0):
                L += 1
            while(L < R) and (nums[R] & 1 == 1):
                R -= 1
            if (L >= R):
                break
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R -= 1
        return nums
