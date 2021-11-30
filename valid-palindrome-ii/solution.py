class Solution:
    def validPalindrome(self, s: str, delete: int = 1) -> bool:
        L, R = 0, len(s) - 1
        while(L < R):
            if (s[L] == s[R]):
                L += 1
                R -= 1
            else:
                if (delete == 0):
                    return False
                else:
                    # Since we can't know which character should delete on left or right,
                    # so try both case.
                    return (self.validPalindrome(s[L:R], 0) or
                            self.validPalindrome(s[L + 1:R + 1], 0))
        return True
