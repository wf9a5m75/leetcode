class Solution:
    def longestPalindrome(self, s: str) -> str:
        #
        # (1) Since the matcher algorithm can detect only odd palindrome,
        #     bind each character with "#"(dummy character)
        s = "#{}#".format("#".join(s))


        n = len(s)
        ans = s[0]
        maxJ = 0

        # The variable R keeps how many characters are palindrome last time.
        R = [0] * n

        for i in range(n):

            # (2) Is there palindrome?
            #
            j = R[i]
            isPalindrome = True
            while(i - j >= 0) and (i + j < n) and (s[i - j] == s[i + j]):
                j += 1

            if j == R[i]:
                continue

            # (3) Keep the palindrome if longer than current
            if j > maxJ:
                ans = s[i - j + 1 : i + j]
                maxJ = j
                # print(ans, maxJ)


            # (4) Since we already know the same characters exist in mirror position,
            #  copy the information from left to right
            while(j > 0):
                j -= 1
                R[i + j] = R[i - j]

        # print(*R)
        return ans.replace("#", "")
