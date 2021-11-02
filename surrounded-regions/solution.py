class Solution:
    def protectOcells(self, board: List[List[str]], y: int, x: int) -> None:
        M, N = len(board), len(board[0])
        if (y < 0) or (y >= M) or (x < 0) or (x >= N):
            return

        if (board[y][x] != "O"):
            return
        board[y][x] = "P"

        deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for delta in deltas:
            self.protectOcells(board, y + delta[0], x + delta[1])


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        newBoard = [["X"] * M for _ in range(N)]

        for y in range(M):
            if (board[y][0] == "O"):
                self.protectOcells(board, y, 0)
            if (board[y][N - 1] == "O"):
                self.protectOcells(board, y, N - 1)
        for x in range(N):
            if (board[0][x] == "O"):
                self.protectOcells(board, 0, x)
            if (board[M - 1][x] == "O"):
                self.protectOcells(board, M - 1, x)

        for y in range(M):
            for x in range(N):
                if board[y][x] == "O":
                    board[y][x] = "X"
                elif board[y][x] == "P":
                    board[y][x] = "O"
        
