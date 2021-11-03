class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        startY = endY = -1
        M, N = len(matrix), len(matrix[0])
        for y in range(M):
            if matrix[y][0] <= target:
                startY = y
            if matrix[y][-1] >= target:
                endY = y
                break

        if (matrix[startY][-1] < target < matrix[endY][0]):
            # target = 12
            # [
            #   [1,3,10,11],
            #   [13,13,13,13],
            #   [14,14,14,14]
            # ]
            return False

        if (matrix[startY][-1] == target) or (matrix[endY][0] == target):
            # target = 12
            # [
            #   [1,3,10,12],
            #   [12,13,13,13],
            #   [14,14,14,14]
            # ]
            return True

        L = 0
        R = N - 1
        while(L != R):
            mid = (L + R) >> 1
            if (matrix[startY][mid] == target):
                return True
            elif (matrix[startY][mid] < target):
                L = mid + 1
            else:
                R = mid
        return False
