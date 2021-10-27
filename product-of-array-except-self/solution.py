class Solution:
    def productExceptSelf_another(self, nums: List[int]) -> List[int]:
        """
        1 1 1 1
        ---[prefix]
          i=0, prefix=1,  1 1 1 1
          i=1, prefix=1,  1 1 1 1
          i=2, prefix=2,  1 1 1 1
          i=3, prefix=6,  1 1 2 1
        ---[postfix]
          j=3, postfix=1,  1 1 2 6
          j=2, postfix=4,  1 1 2 6
          j=1, postfix=12,  1 1 8 6
          j=0, postfix=24,  1 12 8 6
        ---[result]
           24 12 8 6

        """
        res = [1] * len(nums)
        print(*res)

        print("---[prefix]")
        prefix = 1
        for i in range(len(nums)):
            print("  i={}, prefix={}, ".format(i, prefix), *res)
            res[i] = prefix
            prefix *= nums[i]

        print("---[postfix]")
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            print("  j={}, postfix={}, ".format(j, postfix), *res)
            res[j] *= postfix
            postfix *= nums[j]

        print("---[result]")
        print("  ", *res)
        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProd = 1
        results = [0] * len(nums)
        zeroCnt = 0
        lastZeroIdx = -1
        for i, num in enumerate(nums):
            if num != 0:
                totalProd *= num
            else:
                zeroCnt += 1
                lastZeroIdx = i

        if zeroCnt > 1:
            return results
        if zeroCnt == 1:
            results[lastZeroIdx] = totalProd
            return results

        for i, num in enumerate(nums):
            results[i] = totalProd // num
        return results
