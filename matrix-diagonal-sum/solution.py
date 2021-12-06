class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)

        x1 = 0
        x2 = N - 1
        s = 0
        for i in range(N):
            s += mat[i][x1]
            if (x1 != x2):
                s += mat[i][x2]
            x1 += 1
            x2 -= 1
        return s
