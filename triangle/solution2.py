class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        for y in range(N - 1, 0, -1):
            for x in range(y):
                triangle[y - 1][x] += min(triangle[y][x], triangle[y][x + 1])
        return triangle[0][0]
