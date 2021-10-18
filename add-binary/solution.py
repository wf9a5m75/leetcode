import sys
from io import StringIO
from typing import List

class Solution:
    def addBinary(self, A: str, B: str) -> str:
        # A = "11"
        # B = "1"
        A = list(map(int, A))
        B = list(map(int, B))
        sizeA = len(A)
        sizeB = len(B)
        C = A
        D = B
        if (sizeB < sizeA):
            C = B
            D = A
        for i in range(max(sizeA, sizeB) - min(sizeA, sizeB)):
            C.insert(0, 0)

        carryUp = 0
        sizeC = max(sizeA, sizeB)
        for i in range(sizeC - 1, -1, -1):
            s = C[i] + D[i] + carryUp
            carryUp = s // 2
            C[i] = s & 1
        if carryUp == 1:
            C.insert(0, 1)
        return "".join(map(str, C))

def main():
    A = input().strip()
    B = input().strip()
    result = Solution().addBinary(A, B)
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
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()
    # test8()
