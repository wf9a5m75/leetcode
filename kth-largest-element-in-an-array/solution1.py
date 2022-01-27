import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []

        cnt = 0
        for i, num in enumerate(nums):
            if i < k:
                heapq.heappush(hq, num)
            elif num >= hq[0]:
                heapq.heappushpop(hq, num)

        return hq[0]
