import math
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        stack,res = [],-1
        n = len(matrix)
        for i in matrix:
            for j in i:
                heapq.heappush(stack,j)
                # print(stack)
                if len(stack) > (n*n)-k+1:
                    heapq.heappop(stack)
        return stack[0]



        return matrix[yBase][xBase]
#         x = 0
#         y = 0
#         while(k > 0) and (x < n):
            
