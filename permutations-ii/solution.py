from typing import List

class Solution:

    def generate(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if (n == 1):
            return [nums.copy()]

        results = []

        prev = -11
        for i in range(n):
            if prev != nums[i]:
                tmp = nums.pop(i)
                prev = tmp
                others = self.generate(nums)
                for j in range(len(others)):
                    others[j].insert(0, tmp)
                results += others
                nums.insert(i, tmp)
        return results

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if (n == 1):
            return [nums.copy()]

        nums.sort()
        return self.generate(nums)
