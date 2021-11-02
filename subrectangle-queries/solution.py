class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.matrix = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        y, x = row1, col1
        while(y <= row2):
            x = col1
            while(x <= col2):
                self.matrix[y][x] = newValue
                x += 1
            y += 1

    def getValue(self, row: int, col: int) -> int:
        return self.matrix[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
