import sys
from io import StringIO
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        for curr in nums:
            if val != curr:
                nums[p] = curr
                p += 1

        # 1   2   2   3
        # del=1
        # 2   2   3   p   i
        #---------
        # 1   2   2  3
        # del = 2
        # 1   3   p  i
        #---------
        # 1   2   2   3
        # del = 3
        # 1   2   2   p
        return p

def main():
    A = list(map(int, input().split()))
    A.pop(0)
    B = int(input())
    result = Solution().removeElement(A, B)
    A = A[:result]
    A.sort()
    print("{} {}".format(result, " ".join(map(str, A))))

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
    test5()
    test6()
    test7()
    test8()
