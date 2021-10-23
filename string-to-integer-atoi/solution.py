class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        n = len(s)
        isNegative = False

        # (1) skip the leading white spaces
        i = 0
        while(i < n) and (s[i] == ' '):
            i += 1

        # (2) check the sign
        if (i < n) and (s[i] == "+" or s[i] == "-"):
            isNegative = (s[i] == "-")
            i += 1

        # (3) Build the integer
        digitToNum = "0123456789"
        while (i < n) and (s[i].isdigit()):
            # convert one digit to number (just prevent "int()")
            d = 0
            while(s[i] != digitToNum[d]):
                d += 1
            i += 1

            ans = ans * 10 + d
        # (4) Multiply -1 if negative
        if isNegative:
            ans = -ans

        # (5) clip and return the answer
        return max(-2**31, min(2**31 - 1, ans))
        
