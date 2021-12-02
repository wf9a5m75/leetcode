class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        stack = []
        for c in s:
            if c == "(":
                if stack:
                    ans.append(c)
                stack.append(c)
            else:
                if len(stack) > 1:
                    ans.append(c)
                stack.pop()
        return "".join(ans)
