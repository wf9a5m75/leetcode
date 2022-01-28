class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hq = []
        for i, point in enumerate(points):
            d = (abs(point[0]) ** 2 + abs(point[1]) ** 2) ** 0.5
            if i < k:
                heapq.heappush(hq, (-d, i))
            elif (d < -hq[0][0]):
                heapq.heappushpop(hq, (-d, i))
        results = []
        for pointInfo in hq:
            results.append(points[pointInfo[1]])
        return results
