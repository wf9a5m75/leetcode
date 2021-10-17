
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i, val in enumerate(nums):
            mem[val] = i

        for i, val in enumerate(nums):
            rest = target - val
            if (rest in mem):
                j = mem[rest]
                if (i != j):
                    return [min(i, j), max(i, j)]
