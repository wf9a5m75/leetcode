import sys
from io import StringIO
from typing import List

class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # if B does not have any element, just quit this function
        if n == 0:
            return
        # if A does not have any elements, just copy B to A, then quit
        if m == 0:
            for i in range(n):
                A[i] = B[i]
            return


        # the pointer to store value
        k = m + n - 1
        m -= 1
        n -= 1

        # -[before]-----
        # A = 1 2 3 0 0 0
        #         i
        #               k
        # B = 2 5 6
        #         j
        # -[after]-----
        # A = 1 2 2 3 5 6
        #     i
        #               k
        # B = 2 5 6
        #   j

        while(m >= 0) and (n >= 0):
            if A[m] >= B[n]:
                A[k] = A[m]
                m -= 1
            else:
                A[k] = B[n]
                n -= 1
            k -= 1

        # Then copy the rest of values
        # restArr = A
        # restIdx = m
        # if (n > -1):
        #     restArr = B
        #     restIdx = n
        # while(restIdx >= 0):
        #     A[k] = restArr[restIdx]
        #     k -= 1
        #     restIdx -= 1

        # Then copy the rest of values (python technique)
        A[:n + 1] = B[:n+1]






def main():
    A = list(map(int, input().split()))
    m = A.pop(0)
    B = list(map(int, input().split()))
    n = B.pop(0)
    k = m + n
    for i in range(len(A), k):
        A.append(0)

    Solution().merge(A, m, B, n)
    print("{} {}".format(len(A), " ".join(map(str, A))))

def test(testName, inputFile, outputFile):
    capture = StringIO()
    sys.stdin = open(inputFile)
    sys.stdout = capture
    try:
        main()
    except Exception as e:
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        print("[{0}] -> fail".format(testName))
        print(capture.getvalue())

        raise e
        return

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
    # test4()
    # test5()
    # test6()
    # test7()
    # test8()
