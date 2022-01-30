class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        hq = []
        for i, num in enumerate(nums):
            if i < k:
                heapq.heappush(hq, (num, i))
            elif num > hq[0][0]:
                heapq.heappushpop(hq, (num, i))

        hq.sort(key = lambda x : x[1])
        results = []
        for num,idx in hq:
            results.append(num)
        return results
