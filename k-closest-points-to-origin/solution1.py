import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #
        # Time complexity:  O(N log k)
        # Space complexity : O(k)

        # math.sqrt(n) = 2**(0.5 * math.log2(n))
        def calcDistance(point: List[int]) -> int:
            # return 2 ** (0.5 * math.log2(point[0] ** 2 + point[1] ** 2))
            return math.sqrt(point[0] ** 2 + point[1] ** 2)

        # We build a heap queue for the first K elements.
        # Note that python's heapq implements the Minumum Heap,
        # but we want to implement the Maximum Heap.
        # Therefore, we product -1
        heap = [ (-calcDistance(points[i]), i) for i in range(k)]
        heapq.heapify(heap)

        # The rest of array, we compare the the kth farthest point,
        # and if another point is more closer, we just swap them.
        N = len(points)
        for i in range(k, N):
            dist = calcDistance(points[i])
            if dist < -heap[0][0]:
                heapq.heappushpop(heap, (-dist, i))
        return [points[i] for dist, i in heap]
        
