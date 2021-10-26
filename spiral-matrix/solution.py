from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        H, W = len(matrix), len(matrix[0])

        results = []
        left = top = 0
        right = W
        bottom = H

        while(left < right) and (top < bottom):
            for x in range(left, right):
                results.append(matrix[top][x])
            top += 1

            for y in range(top, bottom):
                results.append(matrix[y][right - 1])
            right -= 1

            if (left >= right) or (top >= bottom):
                return results

            for x in range(right - 1, left - 1, -1):
                results.append(matrix[bottom - 1][x])
            bottom -= 1

            for y in range(bottom - 1, top - 1, -1):
                results.append(matrix[y][left])
            left+=1

        return results


    def spiralOrder_slow(self, matrix: List[List[int]]) -> List[int]:

        H, W = len(matrix), len(matrix[0])

        def oneSpiral(startX, startY):
            results = []

            xL, yT = startX, startY
            xR, yB = W - xL - 1, H -yT - 1

            if (xR - xL > 0) and (yB - yT > 0):
                """
                1→→→→2
                ↑    ↓
                ↑    ↓
                4←←←←3
                """
                for x in range(xL, xR):
                    results.append(matrix[startY][x])
                for y in range(yT, yB):
                    results.append(matrix[y][xR])
                for x in range(xR, xL, -1):
                    results.append(matrix[yB][x])
                for y in range(yB, yT, -1):
                    results.append(matrix[y][xL])

            else:
                if (xR - xL == 0):
                    for y in range(yT, yB + 1):
                        if (y < H) and (xL < W):
                            results.append(matrix[y][xL])
                elif (yB - yT == 0):
                    for x in range(xL, xR + 1):
                        if (yT < H) and (x < W):
                            results.append(matrix[yT][x])


            return results

        results = []
        for i in range(min(W // 2, H // 2) + 1):
            results += oneSpiral(i, i)

        return results
