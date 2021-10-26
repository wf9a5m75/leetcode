from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left = top = 0
        bottom = right = n

        matrix = [[0] * n for i in range(n)]
        i = 1
        while(left < right) and (top < bottom):
            for x in range(left, right):
                matrix[top][x] = i
                i += 1
            top += 1

            for y in range(top, bottom):
                matrix[y][right - 1] = i
                i += 1
            right -= 1

            if (left >= right) or (top >= bottom):
                break

            for x in range(right - 1, left - 1, -1):
                matrix[bottom - 1][x] = i
                i += 1
            bottom -= 1

            for y in range(bottom - 1, top - 1, -1):
                matrix[y][left] = i
                i += 1
            left += 1

        return matrix
