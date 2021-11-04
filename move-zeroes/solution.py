class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        lastNonZero = 0
        lastZero = 0
        while(lastNonZero < n):
            while(lastNonZero < n) and (nums[lastNonZero] == 0):
                lastNonZero += 1
            if (lastNonZero < n):
                nums[lastZero], nums[lastNonZero] = nums[lastNonZero], nums[lastZero]
                lastZero += 1
                lastNonZero += 1


    def moveZeroes_acceptable_but_slow(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        while(i < n):
            if (nums[i] == 0):
                nums.pop(i)
                nums.append(0)
                n -= 1
            else:
                i += 1
        
