from typing import List
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        path = []

        matrixSize = rows * cols
        direction = 1
        distance = 1
        x, y = cStart, rStart
        while(len(path) < matrixSize):

            for i in range(distance):
                if (0 <= x < cols) and (0 <= y < rows):
                    path.append((y, x))
                x += direction


            for i in range(distance):
                if (0 <= x < cols) and (0 <= y < rows):
                    path.append((y, x))
                y += direction

            distance += 1
            direction *= -1
        return path




    def spiralMatrixIII_slow(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        path = []
        x = cStart
        y = rStart
        left, top = x - 1, y - 1
        right, bottom = x + 1, y + 1

        hasAppend = True
        while(hasAppend):

            hasAppend = False
            # move to right
            x = max(x, 0)
            while(x < right):
                if (x >= 0 and x < cols) and (y >= 0 and y < rows):
                    path.append((y, x))
                    hasAppend = True
                x += 1
            top -= 1

            # move to bottom
            y = max(y, 0)
            while(y < bottom):
                if (x >= 0 and x < cols) and (y >= 0 and y < rows):
                    path.append((y, x))
                    hasAppend = True
                y += 1
            right += 1

            # move to left
            x = min(x, cols - 1)
            while(x > left):
                if (x >= 0 and x < cols) and (y >= 0 and y < rows):
                    path.append((y, x))
                    hasAppend = True
                x -= 1

            bottom += 1


            # move to top
            y = min(y, rows - 1)
            while(y > top):
                if (x >= 0 and x < cols) and (y >= 0 and y < rows):
                    path.append((y, x))
                    hasAppend = True
                y -= 1
            left -= 1

            x += 1
            y += 1


        return path
            
