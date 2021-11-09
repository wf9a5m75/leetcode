class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        N = len(arr)
        rightMax = arr[N - 1]
        arr[N - 1] = -1
        i = N - 2
        while(i >= 0):
            val = arr[i]
            arr[i] = rightMax
            rightMax = max(rightMax, val)
            i -= 1
        return arr
