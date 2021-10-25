from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if (n == 1):
            return [nums.copy()]

        # if (n == 2):
        #     return [nums.copy(), [nums[1], nums[0]]]

        results = []
        for i in range(n):
            tmp = nums.pop(i)

            others = self.permute(nums)
            for j in range(len(others)):
                others[j].insert(0, tmp)
            results += others

            nums.insert(i, tmp)
        return results
