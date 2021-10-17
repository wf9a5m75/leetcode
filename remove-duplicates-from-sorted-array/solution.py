import sys
from io import StringIO

class Solution:
    def removeDuplicates(self, A) -> int:
        sizeA = len(A)
        if sizeA < 2:
            return len(A)
        if (sizeA == 2) and (A[0] == A[1]):
            return 1
        k = 0
        j = 1
        while(j < sizeA):

            while(j < sizeA) and (A[k] != A[j]):
                j += 1
                k += 1

            if (j >= sizeA):
                break
            if (A[k] == A[j]):
                # 1 2 2 3
                #   k j
                while(j < sizeA) and (A[k] == A[j]):
                    j += 1

                if (j >= sizeA):
                    break
                k += 1
                A[k] = A[j]

        return k + 1

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/1521555/Simple-Python-99-Faster-79-Storage
class OtherSolution:
    def removeDuplicates(self, A) -> int:
        nextP = 0
        for i in range(len(A)):
            if A[i] != A[nextP]:
                nextP += 1
                A[nextP] = A[i]
        return nextP + 1


def main():
    A = list(map(int, input().split()))
    A.pop(0)
    result = Solution().removeDuplicates(A)
    print("{} {}".format(result, " ".join(map(str, A[:result]))))

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
