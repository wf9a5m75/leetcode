class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        M, N = len(mat), len(mat[0])

        startX, startY = 0, M - 1
        while(startX < N):
            x, y = startX, startY
            buffer = []
            while(x < N) and (y < M):
                buffer.append(mat[y][x])
                x += 1
                y += 1

            buffer.sort(reverse=True)

            x, y = startX, startY
            while(x < N) and (y < M):
                mat[y][x] = buffer.pop()
                x += 1
                y += 1
            if (startY > 0):
                startY -= 1
            else:
                startX += 1
        return mat
