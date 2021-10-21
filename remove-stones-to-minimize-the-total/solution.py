import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        n = len(piles)
        piles = list(map(lambda x: -x, piles))
        # print(*pileStates)
        heapq.heapify(piles)

        # piles[0] appears always the highest pile
        for i in range(k):
            heapq.heapreplace(piles, piles[0] + (-piles[0] >> 1) )

        # -------------
        #  Below code is also fine, but slower than heapq.heapreplace
        # -------------
        # while(k > 0):
        #     # Choose the highest pile
        #     stones = heapq.heappop(piles)
        #     remove = (-stones >> 1)
        #     stones += remove
        #     heapq.heappush(piles, stones)
        #     k -= 1

        total = -sum(piles)
        return total
