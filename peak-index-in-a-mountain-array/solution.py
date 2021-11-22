class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        N = len(arr)
        L, R = 0, N - 1
        while(L != R):
            mid = (L + R) >> 1
            if (arr[mid] > arr[mid + 1]):
                R = mid
            else:
                L = mid + 1
        return L
