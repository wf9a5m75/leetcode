import re
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dp3x3 = [set() for _ in range(9)]
        dpRow = [set() for _ in range(9)]
        dpCol = [set() for _ in range(9)]

        for y in range(9):
            for x in range(9):
                if (board[y][x] != "."):
                    val = board[y][x]

                    # Check repetition in 3x3 sub array
                    idx = (y // 3) * 3 + (x // 3)
                    if val in dp3x3[idx]:
                        return False
                    dp3x3[idx].add(val)

                    # Check repetition in rows
                    if val in dpRow[y]:
                        return False
                    dpRow[y].add(val)

                    # Check repetition in columns
                    if val in dpCol[x]:
                        return False
                    dpCol[x].add(val)

        return True


        
