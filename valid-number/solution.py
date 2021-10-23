import sys
from io import StringIO

class Solution:
    def isNumber(self, s: str) -> bool:
        n = len(s)
        hasE = False
        hasDot = False
        hasNum = False
        hasSign = False

        start = 0
        if s[0] == "+" or s[0] == "-":
            # "+9" and "-9" are acceptable
            start += 1
            hasSign = True

        if s[start] == ".":
            # ".9" and "-.9" are acceptable
            start += 1
            hasDot = True

        for i in range(start, n):
            isDot = s[i] == "."
            isE = s[i] in "eE"
            isSign = s[i] in "+-"
            isDigit = s[i].isdigit()

            if (
                # "w", etc
                (isDigit == isDot == isE == isSign == False) or

                # 3.4.5
                (hasDot and isDot) or

                # 35e3e3
                (hasE and isE) or

                # e43
                (hasNum == False and isE) or

                # 6+1
                (hasNum and isSign) or

                #.-4
                (hasDot and hasE == False and isSign) or

                # 99e2.5
                (hasE and isDot) or

                # ++3, 2e3++3, -+3
                (isSign and hasSign)
            ):
                return False
            hasNum = hasNum | isDigit
            hasDot = hasDot | isDot

            hasE = hasE | isE
            if (isE):
                hasSign = False
                hasNum = False

        # 23e -> False
        return hasNum


def main():
    A = input()
    result = Solution().isPalindrome(A)
    print(int(result))

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
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()
    # test8()
