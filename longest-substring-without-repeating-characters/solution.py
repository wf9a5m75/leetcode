class Solution:
    def lengthOfLongestSubstring(self, A: str) -> int:

        L = 0
        R = 0
        N = len(A)
        maxLen = 0
        mem = set()
        while(R < N):
            if (L == R):
                R += 1
            mem.add(A[L])
            while(R < N) and (A[R] not in mem):
                mem.add(A[R])
                R+=1
            # print(L, R, "->", R- L)
            maxLen=max(maxLen, R - L)
            mem.remove(A[L])
            L += 1

        return maxLen
