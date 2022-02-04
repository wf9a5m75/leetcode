class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)

        mem = {0: -1}
        total = 0
        maxLen = 0
        for i in range(n):
            if nums[i] == 0:
                total -= 1
            else:
                total += 1
            if total in mem:
                maxLen = max(maxLen, i - mem[total])
            else:
                mem[total] = i
        return maxLen
