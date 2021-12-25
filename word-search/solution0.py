from test import checkTests
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        M, N = len(board), len(board[0])
        visited = [[False] * N for _ in range(M)]

        wordN = len(word)
        directions = [(-1,0), (1,0),(0, -1), (0, 1)]

        def dfs(y: int, x : int, i: int) -> bool:
            if i + 1 == wordN:
                return True

            nextW = word[i + 1]
            for direction in directions:
                dy = y + direction[0]
                dx = x + direction[1]
                if ((0 <= dy < M) and (0 <= dx < N) and
                    (board[dy][dx] == nextW) and
                    (visited[dy][dx] == False)):

                    visited[dy][dx] = True
                    if dfs(dy, dx, i + 1):
                        return True
                    visited[dy][dx] = False

            return False

        for y in range(M):
            for x in range(N):
                if (board[y][x] == word[0]):
                    visited[y][x] = True
                    if dfs(y, x, 0):
                        return True
                    visited[y][x] = False

        return False

checkTests(Solution().exist)
