class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #
        #   Greedy
        #       O(n log n) time
        #       O(1) space
        #
        N = len(points)
        if (N == 1):
            return 1

        # sorting by thier start times
        #   quick sort: O(n log n)
        points.sort(key = lambda point: point[0])

        start = points[0][0]
        end = points[0][1]

        # We need one shot at least
        cnt = 1

        for i in range(1, N):

            # Reduces the end time
            if start <= points[i][0] <= end:
                end = min(end, points[i][1])
                continue

            # If new start position is not covered by the previous range,
            # we need another shot.
            cnt += 1
            start = points[i][0]
            end = points[i][1]
        return cnt

        
