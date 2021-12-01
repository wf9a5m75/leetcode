class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        L, R = 0, len(s) - 1
        while(L < R):
            if (not s[L].isalpha()):
                L += 1
            if (not s[R].isalpha()):
                R -= 1

            if (s[L].isalpha() and s[R].isalpha()):
                s[L], s[R] = s[R], s[L]
                L += 1
                R -= 1
        return "".join(s)

    def reverseOnlyLetters(self, s: str) -> str:

        # picks up only alphabet characters
        stack = []
        for c in s:
            if c.isalpha():
                stack.append(c)

        # Build the answer
        ans = []
        for c in s:
            if c.isalpha():
                # If alphabet, use the stack top
                ans.append(stack.pop())
            else:
                # otherwise, append the character.
                ans.append(c)
        return "".join(ans)
