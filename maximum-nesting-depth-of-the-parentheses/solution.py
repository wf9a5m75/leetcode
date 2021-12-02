class Solution:
    def maxDepth(self, s: str) -> int:
        N = len(s)
        if (s == "") or ((N == 1) and (s != "(" or s != ")")):
            return 0

        stack = []
        maxD = 0
        for c in s:
            if c == "(":
                stack.append(c)
                maxD = max(maxD, len(stack))
            elif (c == ")"):
                if (stack) and (stack[-1] == "("):
                    stack.pop()
                else:
                    # invalid
                    return 0
        if len(stack) == 0:
            return maxD
        else:
            return 0
