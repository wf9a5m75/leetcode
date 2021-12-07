class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        answer = 0
        N = len(grid[0])
        for row in grid:
            L, R = 0, N
            while(L != R):
                mid = (L + R) >> 1
                if (row[mid] >= 0):
                    L = mid + 1
                else:
                    R = mid
            if (L < N):
                answer += N - L
        return answer
                
