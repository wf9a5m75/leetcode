class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)

        #---------------------------
        # Find the duplicate number using negative marking algorithm
        # https://leetcode.com/problems/find-the-duplicate-number/solution/
        #---------------------------
        duplicatedVal = 0
        for num in nums:
            curr = abs(num) - 1
            if nums[curr] < 0:
                duplicatedVal = curr + 1
                break
            nums[curr] = -nums[curr]

        #---------------------------
        # Find the missing number
        #---------------------------

        # Since all numbers, except duplicated number and missing numbers, appear once
        # we can use summution
        s = (N * (N + 1)) // 2
        for num in nums:
            if (num < 0):
                # Some values are negative, because we changed the sign above.
                num = -num
            s -= num

        # The duplicate number is calcurated twice,
        # put it back.
        # Then rest of value is the missing number
        s += duplicatedVal

        return [duplicatedVal, s]
        
