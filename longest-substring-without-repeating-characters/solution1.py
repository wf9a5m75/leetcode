class Solution:
    def lengthOfLongestSubstring(self, A: str) -> int:

        N = len(A)
        mem = set()
        maxLen = 0
        L = R = 0
        while(R < N):

            # Record characters into the mem set
            while(R < N) and (A[R] not in mem):
                mem.add(A[R])
                R += 1

            # Calcurate substring length
            maxLen = max(maxLen, R - L)

            # Remove until the character same with A[R]
            while(L < R < N) and (A[L] != A[R]):
                mem.remove(A[L])
                L += 1

            # Move the L pointer to not A[R]
            while(L < R < N) and (A[L] == A[R]):
                L += 1
            R += 1

        return maxLen
