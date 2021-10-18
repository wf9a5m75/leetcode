import sys
from io import StringIO
from typing import List

class Solution:
    def mySqrt(self, x: int) -> int:
        if (x == 0):
            return 0
        if (x < 4):
            return 1

        # x = 8, left = 1, right = 4
        left = 1
        right = x >> 1
        while(left != right):
            # mid = (1 + 4) >> 1 = 2
            # mid = (2 + 4) >> 1 = 3
            mid = (left + right) >> 1

            # s = 2 * 2 = 4
            # s = 3 * 3 = 9
            s = mid * mid

            # 4 < 8
            # 9 > 8
            if s == x:
                return mid
            elif s < x:
                # left = 2
                left = mid + 1
            else:
                # right = mid - 1 = 2
                right = mid

        if (left * left > x):
            # because sqrt(x) exists between left - 1 and left
            left -= 1
        return left


def main():
    A = int(input())
    result = Solution().mySqrt(A)
    print(result)

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
    test1()
    test2()
    test3()
    test4()
    # test5()
    # test6()
    # test7()
    # test8()
