class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        M, N = len(word1), len(word2)
        p1 = p2 = 0
        while(p1 < M) and (p2 < N):
            result.append(word1[p1])
            result.append(word2[p2])
            p1 += 1
            p2 += 1
        while(p1 < M):
            result.append(word1[p1])
            p1 += 1
        while(p2 < N):
            result.append(word2[p2])
            p2 += 1
        return "".join(result)
