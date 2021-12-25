from test import checkTests
from collections import deque, Counter
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])

        # Creates a Trie tree
        #   Space complexity: O(M * N)
        dp = [[{"visited": False} for n in range(N)] for m in range(M)]
        startPositions = deque()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Build the character graph map.
        #   Time complexity: O(M * N)
        wordCounter = Counter(word)
        for y in range(M):
            for x in range(N):
                char = board[y][x]
                if (char in wordCounter):
                    wordCounter[char] -= 1

                    # Records the start position
                    if char == word[0]:
                        startPositions.append((y, x, 0))

                    for dy, dx in directions:
                        if (0 <= y + dy < M) and (0 <= x + dx < N):
                            positions = (dp[y + dy][x + dx].get(char, []))
                            positions.append((y, x))
                            dp[y + dy][x + dx][char] = positions


        # Does this board have necessary number of characters?
        # If any characters in wordCounter still have greater than 0,
        # this board does not have enough number of characters.
        for char in wordCounter:
            if wordCounter[char] > 0:
                return False

        # DFS
        #   Time complexity: O(length of the word * number of the first character)
        wordLen = len(word)
        def dfs(y: int, x: int, currIdx: int) -> bool:

            # If we check all characters, return true
            if (currIdx + 1 == wordLen):
                return True
            dp[y][x]["visited"] = True

            # Do neighbors have the next character?
            nextChar = word[currIdx + 1]
            for dy, dx in (dp[y][x].get(nextChar, [])):

                if dp[dy][dx]["visited"]:
                    continue
                if dfs(dy, dx, currIdx + 1):
                    return True

            dp[y][x]["visited"] = False
            return False

        # Starts from all start positions
        while(startPositions):
            curr = startPositions.popleft()
            if dfs(*curr):
                return True

        return False

checkTests(Solution().exist)
