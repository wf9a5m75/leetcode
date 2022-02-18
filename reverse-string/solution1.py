class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)
        def reverse(i: int, j: int):
            if (i >= j):
                return
            s[i],s[j] = s[j], s[i]
            reverse(i + 1, j - 1)
        reverse(0, N - 1)
