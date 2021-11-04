class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        isSuccess = True
        j = i = 0
        sizeS = len(s)
        sizeT = len(t)
        while(i < sizeT) and (j < len(s)):
            if t[i] == s[j]:
                j+=1
            i += 1
        return sizeS == j
