class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows, cols = len(rowSum), len(colSum)
        A = [[0] * cols for _ in range(rows)]

        for y in range(rows):
            for x in range(cols):
                A[y][x] = min(rowSum[y], colSum[x])
                rowSum[y] -= A[y][x]
                colSum[x] -= A[y][x]
        return A
