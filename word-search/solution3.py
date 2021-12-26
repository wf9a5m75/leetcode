from test import checkTests
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])

        trie = {}
        parent = trie
        for w in word:
            parent[w] = {"eow": False}
            parent = parent[w]
        parent["eow"] = True

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def searchWord(parent: dict, y: int, x: int) -> bool:

            boardLabel = board[y][x]
            parent = parent[boardLabel]
            if (parent["eow"]):
                return True

            board[y][x] = "!"

            for dy, dx in directions:
                dy += y
                dx += x
                if (0 <= dy < M) and (0 <= dx < N) and (board[dy][dx] in parent):
                    if searchWord(parent, dy, dx):
                        return True
            board[y][x] = boardLabel

            return False

        for y in range(M):
            for x in range(N):
                if (board[y][x] in trie) and (searchWord(trie, y, x)):
                    return True

        return False

checkTests(Solution().exist)
