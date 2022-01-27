class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)

        while(len(stones) > 1):

            top1 = heapq.heappop(stones)
            top2 = heapq.heappop(stones)
            if top1 != top2:
                heapq.heappush(stones, top1 - top2)
        if (len(stones) == 1):
            return -stones[0]
        else:
            return 0
