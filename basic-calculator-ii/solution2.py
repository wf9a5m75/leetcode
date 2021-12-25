from test import checkTests
from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        #
        #  Parse the string s
        #
        #  s = " 4 +  3*5 / 2 * 4 / 5 - 10"
        #    ↓
        #  query = [4, '+', 3, '*', 5, '/', 2, '*', 4, "/", 5, "-", 10]
        #
        s += "$"
        stack = [0]
        num = 0
        currentOp = "+"
        for char in s:
            if (char == " "):
                continue
            if (char.isdigit()):
                num = num * 10 + int(char)
            else:
                if (currentOp == "*"):
                    stack.append(stack.pop() * num)
                elif (currentOp == "/"):
                    stack.append(int(stack.pop() / num))
                elif (currentOp == "+"):
                    stack.append(num)
                elif (currentOp == "-"):
                    stack.append(-num)

                num = 0
                currentOp = char

        return sum(stack)

def wrap(s: str) -> int:
    return Solution().calculate(s)
checkTests(wrap)
