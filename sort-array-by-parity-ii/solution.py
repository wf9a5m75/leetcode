class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ptrEven = 0
        ptrOdd = 1
        N = len(nums)

        while(ptrEven < N) and (ptrOdd < N):
            while(ptrEven < N) and (nums[ptrEven] & 1 == 0):
                ptrEven += 2

            while(ptrOdd < N) and (nums[ptrOdd] & 1 == 1):
                ptrOdd += 2

            if (ptrEven < N) and (ptrOdd < N):
                nums[ptrEven], nums[ptrOdd] = nums[ptrOdd], nums[ptrEven]
                ptrOdd += 2
                ptrEven += 2
        return nums
