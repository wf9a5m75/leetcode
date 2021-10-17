class Solution:
    def maskWords(self, A: str, B: str) -> str:
        sizeA = len(A)
        sizeB = len(B)
        i = 0
        limit = min(sizeA, sizeB)
        while(i < limit) and (A[i] == B[i]):
            i += 1
        if i == 0:
            return ""
        return A[:i]
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = strs.pop(0)
        i = 0
        N = len(strs)
        while(i < N) and (len(commonPrefix) > 0):
            commonPrefix = self.maskWords(commonPrefix, strs[i])
            i += 1

        return commonPrefix
