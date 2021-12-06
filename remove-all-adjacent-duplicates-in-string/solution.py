class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [""]
        for c in s:
            if stack[-1] != c:
                stack.append(c)
            else:
                stack.pop()
        return "".join(stack)
                
