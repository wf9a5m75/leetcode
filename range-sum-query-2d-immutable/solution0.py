class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        M = len(matrix[0])
        N = len(matrix)
        self.matrix = matrix

        for y in range(N):
            for x in range(1, M):
                self.matrix[y][x] += self.matrix[y][x - 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        s = 0
        for y in range(row1, row2 + 1):
            if (col1 > 0):
                s -= self.matrix[y][col1 - 1]
            s += self.matrix[y][col2]
        return s
            
