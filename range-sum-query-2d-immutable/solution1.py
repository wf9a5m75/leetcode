class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        M = len(matrix[0])
        N = len(matrix)
        self.dp = [[0] * M for _ in range(N)]

        for y in range(N):
            for x in range(M):
                self.dp[y][x] = matrix[y][x]
                if (y - 1 >= 0):
                    self.dp[y][x] += self.dp[y - 1][x]
                if (x - 1 >= 0):
                    self.dp[y][x] += self.dp[y][x - 1]
                if (y - 1 >= 0) and (x - 1 >= 0):
                    self.dp[y][x] -= self.dp[y - 1][x - 1]
            # print(self.dp[y])



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = self.dp[row2][col2]
        if (row1 - 1 >= 0):
            s -= self.dp[row1 - 1][col2]
        if (col1 - 1 >= 0):
            s -= self.dp[row2][col1 - 1]
        if (row1 - 1 >= 0) and (col1 - 1 >= 0):
            s += self.dp[row1 - 1][col1 - 1]

        return s




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
