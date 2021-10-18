class Solution:
    def searchInsert(self, A: List[int], B: int) -> int:

        L = 0
        R = len(A)
        while(L != R):
            mid = (L + R) >> 1
            if (A[mid] < B):
                L = mid + 1
            else:
                R = mid
        return L
