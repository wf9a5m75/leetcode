import re
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def isValid3x3(top: int, left: int) -> bool:
            txt = ""
            for i in range(3):
                row = board[top + i]
                txt += "".join(row[left: left + 3])
            txt = "".join(txt)
            if (re.search(r"(.).*?\1", txt)):
                return False
            return True


        # Replace "." to ""
        N = len(board)
        for y in range(N):
            board[y] = list(map(lambda x: x if x.isdigit() else "", board[y]))


        # check the duplicates for row and columns
        columns = [set() for i in range(9)]
        for y in range(N):
            row = board[y]
            rowStr = "".join(row)
            if (re.search(r"(.).*?\1", rowStr)):
                return False
            for i in range(9):
                if row[i] == "":
                    continue
                if (row[i] in columns[i]):
                    return False
                columns[i].add(row[i])


        for y in range(3):
            for x in range(3):
                if not isValid3x3(y * 3, x * 3):
                    return False
        return True
