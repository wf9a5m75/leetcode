class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        currStr = ""
        currNum = 0
        for char in s:
            if char.isalpha():
                currStr += char
            elif char.isnumeric():
                currNum = currNum * 10 + int(char)
            elif char == "[":
                stack.append(currStr)
                stack.append(currNum)
                currStr = ""
                currNum = 0
            else:
                currNum = stack.pop()
                buffer = currStr * currNum
                currStr = ""
                currNum = 0
                if (stack):
                    currStr = stack.pop()
                currStr += buffer

        return currStr
