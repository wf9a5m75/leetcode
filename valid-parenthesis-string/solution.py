import sys
from io import StringIO

class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}

        def backtracking(L: int, start: int) -> bool:
            key = "{}:{}".format(L, start)
            if (key in dp):
                return dp[key]

            # print(L, start)
            for i in range(start, len(s)):
                if (s[i] == "("):
                    L += 1
                elif (s[i] == "*"):
                    result = backtracking(L + 1, i + 1)

                    if (result == False) and (L > 0):
                        result = backtracking(L - 1, i + 1)

                    if (result == False):
                        result = backtracking(L, i + 1)

                    dp[key] = result
                    return result
                else:
                    L -= 1
                    if (L < 0):
                        dp[key] = False
                        return False

            dp[key] = (L == 0)
            return dp[key]

        return backtracking(0, 0)



def main():
    A = input()
    print(Solution().checkValidString(A))

def test(testName, inputFile, outputFile):
    capture = StringIO()
    sys.stdin = open(inputFile)
    sys.stdout = capture
    main()
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__
    results = capture.getvalue().split("\n")


    fAnsFile = open(outputFile)
    i = 0
    passTheTest = True
    lenResults = len(results)
    for ansLine in fAnsFile:
        ansLine = ansLine.strip()
        if ansLine != results[i].strip():
            results[i] = "-->|" + results[i]
            passTheTest = False
        else:
            results[i] = "   |" + results[i]

        i += 1
        if i == lenResults:
            break
    if ((not passTheTest) or (i + 1 != len(results))):
        print("[{0}] -> fail".format(testName))
        print("\n".join(results))
    else:
        print("[{0}] -> pass".format(testName))

    fAnsFile.close()
    capture.close()


def test10():
    test("test10", "input10.txt", "output10.txt")

def test9():
    test("test9", "input09.txt", "output09.txt")

def test8():
    test("test8", "input08.txt", "output08.txt")

def test7():
    test("test7", "input07.txt", "output07.txt")

def test6():
    test("test6", "input06.txt", "output06.txt")

def test5():
    test("test5", "input05.txt", "output05.txt")

def test4():
    test("test4", "input04.txt", "output04.txt")

def test3():
    test("test3", "input03.txt", "output03.txt")

def test2():
    test("test2", "input02.txt", "output02.txt")

def test1():
    test("test1", "input01.txt", "output01.txt")

def test0():
    test("test0", "input00.txt", "output00.txt")

if __name__ == "__main__":
    test0()
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()
