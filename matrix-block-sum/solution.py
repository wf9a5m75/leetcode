class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(mat), len(mat[0])

        ans = [[0] * N for _ in range(M)]

        s = 0
        for i in range(M):
            for j in range(N):
                if i > 0:
                    mat[i][j] += mat[i - 1][j]
                if j > 0:
                    mat[i][j] += mat[i][j - 1]
                if i > 0 and j > 0:
                    mat[i][j] -= mat[i - 1][j - 1]
        print("---------------")
        for row in mat:
            print(*row)
        print("---------------")

        for i in range(M):
            for j in range(N):

                st_i, ed_i = max(0, i - k), min(M - 1, i + k)
                st_j, ed_j = max(0, j - k), min(N - 1, j + k)
                ans[i][j] = mat[ed_i][ed_j]
                if (st_i > 0):
                    ans[i][j] -= mat[st_i - 1][ed_j]
                if (st_j > 0):
                    ans[i][j] -= mat[ed_i][st_j - 1]
                if (st_i > 0) and (st_j > 0):
                    ans[i][j] += mat[st_i - 1][st_j - 1]

        return ans
