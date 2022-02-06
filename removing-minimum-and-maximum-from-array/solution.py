class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        N = len(nums)
        minIdx = maxIdx = 0
        for i in range(N):
            if nums[i] < nums[minIdx]:
                minIdx = i
            elif nums[i] > nums[maxIdx]:
                maxIdx = i

        halfIdx = N // 2
        farFromL = max(minIdx, maxIdx) + 1
        farFromR = max(N - minIdx, N - maxIdx)
        nearFromL = min(minIdx, maxIdx) + 1
        nearFromR = min(N - minIdx, N - maxIdx)

        return min(nearFromL + nearFromR, farFromL, farFromR)
        
