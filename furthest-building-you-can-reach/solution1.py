class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        #
        # Got a TLE
        #
        N = len(heights)

        @lru_cache(2000)
        def dp(i: int, bricks: int, ladders: int)->int:
            if i == N - 1:
                return N - 1

            diff = heights[i + 1] - heights[i]
            farthest = i
            if diff > 0:

                if (ladders > 0):
                    farthest = dp(i + 1, bricks, ladders - 1)

                if (bricks >= diff):
                    farthest = max(farthest, dp(i + 1, bricks - diff, ladders))
            else:
                farthest = dp(i + 1, bricks, ladders)
            return farthest

        return dp(0, bricks, ladders)

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        hq = []

        N = len(heights)
        for i in range(N - 1):
            diff = heights[i + 1] - heights[i]
            if (diff > 0):
                # We record jumping spots
                heapq.heappush(hq, diff)

            if len(hq) > ladders:
                # Choosing the lowest jump spot so far, then we use some bricks for the spot
                bricks -= heapq.heappop(hq)

            if bricks < 0:
                # If bricks are not enough, we can't move ahead.
                return i
        return N - 1
