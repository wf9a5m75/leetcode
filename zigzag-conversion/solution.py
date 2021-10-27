class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1) or (len(s) <= numRows):
            return s

        mem = [[] for i in range(numRows)]

        x = y = 0
        yDirection = 1
        for char in s:
            # print(y)
            mem[y].append(char)
            x += int(yDirection == -1)
            y += yDirection
            if (yDirection * y == numRows - 1) or (y == 0):
                yDirection *= -1

        # for row in mem:
        #     print(row)
        result = "".join(list(map(lambda row: "".join(row), mem)))
        return result
            
