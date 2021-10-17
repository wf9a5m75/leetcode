class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        sizeS = 0
        partners = {
            "(": ")",
            "{": "}",
            "[": "]",
            ")": "(",
            "}": "{",
            "]": "["
        }
        fronts = ["(", "[", "{"]

        for char in s:
            p = partners[char]
            if (char in fronts):
                stack.append(char)
                sizeS += 1
            elif (sizeS > 0) and (stack[-1] == p):
                stack.pop()
                sizeS -= 1
            else:
                return False
        return (sizeS == 0)

ins = Solution()

print("case1", ins.isValid("()") == True)
print("case2", ins.isValid("{}()[]") == True)
print("case3", ins.isValid("{)[]") == False)
print("case4", ins.isValid("[{{()}}]()") == True)
print("case5", ins.isValid("[{}}]()") == False)
