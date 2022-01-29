class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        M, N = len(board[0]), len(board)

        ans = 0
        for y in range(N):
            for x in range(M):
                if (board[y][x] == "X") and (y == 0 or board[y - 1][x] == ".") and (x == 0 or board[y][x - 1] == "."):
                    ans += 1

        return ans

                    
