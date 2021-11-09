class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        N = len(arr)
        i = N - 1
        while(i >= 0):
            if (arr[i] == 0):
                arr.insert(i, 0)
                arr.pop()
            i -= 1
        
