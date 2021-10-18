import sys
from io import StringIO


class Solution:
    def makeNgramHash(self, A, n):
        mem = {}
        for i in range(0, len(A) - n + 1):
            key = A[i: i + n]
            if key not in mem:
                mem[key] = [i]
            else:
                mem[key].append(i)
        return mem
    # @param A : an string
    # @param B : an string
    # @return an integer
    def strStr(self, A, B):

        sizeA = len(A)
        sizeB = len(B)
        if sizeA == 0:
            if sizeB == 0:
                return 0
            else:
                return -1
        if sizeA < sizeB:
            return -1
        if sizeA == 1:
            if sizeB < 2 or A == B:
                return 0
            else:
                return -1

        n = max(sizeB >> 1, 1)
        mem = self.makeNgramHash(A, n)

        i = 0
        while(i <= sizeB - n):
            key = B[i: i + n]
            if (key in mem):
                for startPos in mem[key]:
                    if A[startPos: startPos + sizeB] == B:
                        return startPos
                del mem[key]
            i += 1

        return -1



def main():
    A = input().strip()
    B = input().strip()
    result = Solution().strStr(A, B)
    print(result)

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
        if ansLine != results[i]:
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
