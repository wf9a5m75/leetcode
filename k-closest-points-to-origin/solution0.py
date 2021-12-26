from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        points.sort(key = lambda point: math.sqrt(point[0] ** 2 + point[1] ** 2))
        return points[:k]
