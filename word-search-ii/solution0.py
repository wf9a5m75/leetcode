from test import checkTests
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        M, N = len(board), len(board[0])

        # Build trie tree
        trie = {}
        for word in words:
            parent = trie
            for w in word:
                if w not in parent:
                    parent[w] = {}
                parent = parent[w]
            parent["word"] = word

        results = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def searchWord(parent: dict, y: int, x: int):

            parent = parent[board[y][x]]
            if ("word" in parent):
                results.append(parent["word"])
                del parent["word"]

            # To prevent visiting we already checked,
            # we replace the board value
            tmp = board[y][x]
            board[y][x] = "!"

            for dy, dx in directions:
                dx += x
                dy += y
                if (0 <= dx < N) and (0 <= dy < M) and (board[dy][dx] in parent):
                    searchWord(parent, dy, dx)

            # Restore the board cell
            board[y][x] = tmp


        for y in range(M):
            for x in range(N):
                if (board[y][x] in trie):
                    searchWord(trie, y, x)

        return results

checkTests(Solution().findWords)
