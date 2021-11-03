class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M, N = len(matrix), len(matrix[0])

        hasZeroOnFirstRow = False
        hasZeroOnFirstColumn = False
        x = 0
        while(x < N) and (hasZeroOnFirstRow == False):
            hasZeroOnFirstRow = matrix[0][x] == 0
            x += 1
        y = 0
        while(y < M) and (hasZeroOnFirstColumn == False):
            hasZeroOnFirstColumn = matrix[y][0] == 0
            y += 1

        for y in range(1, M):
            for x in range(1, N):
                if (matrix[y][x] == 0):
                    matrix[y][0] = 0
                    matrix[0][x] = 0


        for y in range(1, M):
            if (matrix[y][0] == 0):
                for x in range(N):
                    matrix[y][x] = 0
        for x in range(1, N):
            if (matrix[0][x] == 0):
                for y in range(M):
                    matrix[y][x] = 0

        if hasZeroOnFirstRow:
            for x in range(N):
                matrix[0][x] = 0
        if hasZeroOnFirstColumn:
            for y in range(M):
                matrix[y][0] = 0
