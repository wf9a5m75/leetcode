class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n-1,-1,-1):
            p = 0
            for j in matrix[i][0:n]:
                matrix[p].append(j)
                matrix[i].pop(0)
                p += 1

#             for row in matrix:
#                 print(*row)
#             print("--" * 10)

            
