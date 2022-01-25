class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = list(word1)
        lenWord1, lenWord2 = len(word1), len(word2)

        @lru_cache(2000)
        def dp(i: int, j: int) -> int:
            if (i == lenWord1):
                return lenWord2 - j
            if (j == lenWord2):
                return lenWord1 - i

            doSomething = 0
            if word1[i] == word2[j]:
                doSomething = dp(i + 1, j + 1)
            else:
                doDelete = dp(i + 1, j)
                doReplace = dp(i + 1, j + 1)
                doInsert = dp(i, j + 1)
                doSomething = 1 + min(doDelete, doReplace, doInsert)
            return doSomething
        return dp(0, 0)
