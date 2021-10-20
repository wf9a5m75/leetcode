class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 2, 7, 4, 1, 8, 1
        #  ↓
        # [8, 7], 4, 2, 1, 1
        #  ↓
        # y = 8, x = 7 -> y = 1 -> put it to the array.
        #  ↓
        # [4, 2], 1, 1, 1
        #  ↓
        # y = 4, x = 2 -> y = 2 -> put it to the array
        #  ↓
        # [2, 1], 1, 1
        #  ↓
        # y = 2, x = 1 -> y = 1 -> put it to the array
        #  ↓
        # [1, 1], 1
        #  ↓
        # y = 1, x = 1, -> y = 0
        #  ↓
        # 1

        # Since python's heapq provides min-heap, not max-heap.
        # That's why heapq.pop() returns smallest one.
        # But we want to obtain the largerst one.
        # To solve this, we flip the signs.
        stones = list(map(lambda x: -x, stones))

        # Builds a heap
        heapq.heapify(stones)

        # Continues the game until the last stone
        while(len(stones) > 1):

            # print(*heapq.nlargest(len(stones), stones))

            # pick top 2 weight stones
            y = heapq.heappop(stones) # -8
            x = heapq.heappop(stones) # -7

            y = y - x  # -1 = (-8) - (-7)
            if (y < 0):
                heapq.heappush(stones, y)

        if len(stones) == 0:
            return 0
        else:
            return -stones[0]
