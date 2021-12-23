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
"""

[1,2,3] ---->  [3,2,1]  ---->  [2,3,1]
 L   R  (swap)  R L     (swap)  R L

[6,1,4,2] --> [6,2,1,4]
     i

[9,0,0]  ----->  [9,0,0] ----->  [9,0, 0]  => (flip) => [0,0,9]
 L   R   (L+=1)     L R  (L+=1)        LR

[1,2,3,2,1] -----> [2,1,1,2,3]
[1,2,3,4,1] -----> [1,2,4,3,1] ---> [1,2,4,1,3]
"""
