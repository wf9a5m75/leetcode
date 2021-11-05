class Solution:

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        M2, N2 = M + 2, N + 2
        INF = 10**5
        result = [[INF] * N2 for _ in range(M2)]
        for x in range(N):
            for y in range(M):
                if (mat[y][x] == 0):
                    result[y + 1][x + 1] = 0

        for y in range(M):
            k = N - 1
            for x in range(N):
                result[y + 1][x + 1] = min(result[y + 1][x + 1],
                                   result[y][x + 1] + 1, result[y + 2][x + 1] + 1,
                                   result[y + 1][x] + 1, result[y + 1][x + 2] + 1)

                result[y + 1][k + 1] = min(result[y + 1][k + 1],
                                   result[y][k + 1] + 1, result[y + 2][k + 1] + 1,
                                   result[y + 1][k] + 1, result[y + 1][k + 2] + 1)

                k -= 1

        for x in range(N):
            k = M - 1
            for y in range(M):
                result[y + 1][x + 1] = min(result[y + 1][x + 1],
                                   result[y + 1][x] + 1, result[y + 1][x + 2] + 1,
                                   result[y][x + 1] + 1, result[y + 2][x + 1] + 1)

                result[k + 1][x + 1] = min(result[k + 1][x + 1],
                                   result[k + 1][x] + 1, result[k + 1][x + 2] + 1,
                                   result[k][x + 1] + 1, result[k + 2][x + 1] + 1)

                k -= 1

        for x in range(N):
            for y in range(M):
                mat[y][x] = result[y + 1][x + 1]
        return mat
