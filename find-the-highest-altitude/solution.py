class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixSum = 0
        ans = 0
        for altitude in gain:
            prefixSum += altitude
            ans = max(ans, prefixSum)
        return ans
