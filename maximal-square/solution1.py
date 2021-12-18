class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #
        # Time complexity: O((M * N) ** 2)
        #

        M = len(matrix)
        N = len(matrix[0])

        ans = 0
        for y in range(M):
            for x in range(N):

                if matrix[y][x] == "0":
                    continue

                #
                # Finding the maximum square from each "1" cell
                #
                #  A  1  1      A  B  1      A  B  C
                #  1  1  1  ->  B  B  1  ->  B  B  C
                #  1  1  1      1  1  1      C  C  C
                extend = 1
                while(x + extend < N) and (y + extend < M):
                    x1, y1 = x + extend, y + extend
                    k = 0
                    while (k <= extend) and (matrix[y1][k + x] == matrix[k + y][x1] == "1"):
                        k += 1

                    if (k > extend):
                        extend += 1
                    else:
                        break
                ans = max(ans, extend)
        return ans * ans
