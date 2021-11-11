class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        results = []
        s = 0
        for num in nums:
            s += num
            results.append(s)
        return results
