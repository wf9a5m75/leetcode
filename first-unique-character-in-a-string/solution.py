class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        alphaIdx = [n + 2] * 26
        ordA = ord('a')
        for j, char in enumerate(s):
            i = ord(char) - ordA
            if alphaIdx[i] == n + 2:
                alphaIdx[i] = j
            else:
                alphaIdx[i] = n + 1

        minIdx = n + 1
        for i in range(26):
            minIdx = min(minIdx, alphaIdx[i])

        return minIdx if minIdx < n else -1
