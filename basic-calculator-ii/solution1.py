from test import checkTests

class Solution:
    def calculate(self, s: str) -> int:
        #
        #  Parse the string s
        #
        #  s = " 4 +  3*5 / 2 * 4 / 5 - 10"
        #    ↓
        #  query = [4, '+', 3, '*', 5, '/', 2, '*', 4, "/", 5, "-", 10]
        #
        query = []
        num = 0
        for char in s:
            if (char == " "):
                continue
            if (char.isdigit()):
                num = num * 10 + int(char)
            else:
                query.append(num)
                query.append(char)
                num = 0
        query.append(num)


        #  query = [4, '+', 3, '*', 5, '/', 2, '*', 4]

        # Calculates "*" and "/" operators
        i = 0
        nextQ = []
        N = len(query)
        while(i < N):
            if query[i] == "*":
                nextQ.append(nextQ.pop() * query[i + 1])
                i += 2
            elif query[i] == "/":
                nextQ.append(int(nextQ.pop() / query[i + 1]))
                i += 2
            else:
                nextQ.append(query[i])
                i += 1

        # Calculates "+" and "-" operators
        ans = nextQ.pop(0)
        N = len(nextQ)
        i = 0
        while(i < N):
            if nextQ[i] == "+":
                ans += nextQ[i + 1]
                i += 2
            else:
                ans -= nextQ[i + 1]
                i += 2
        return ans

def wrap(s: str) -> int:
    return Solution().calculate(s)
checkTests(wrap)
