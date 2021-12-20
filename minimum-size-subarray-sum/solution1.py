import sys
from io import StringIO
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        R = s = 0
        N = len(nums)
        ans = N + 1
        while(R < N):
            s += nums[R]
            R += 1

            if (s >= target):
                while (s - nums[L] >= target):
                    s -= nums[L]
                    L += 1

                ans = min(ans, R - L)
                # print("--->ans = ", ans, s, nums[L:R])

                # short cut optimization.
                if ans == 1:
                    return 1

        if ans == N + 1:
            return 0
        else:
            return ans
            
    def minSubArrayLen_another(self, target: int, nums: List[int]) -> int:
        L = 0
        R = s = 0
        N = len(nums)
        ans = N + 1
        for R, val in enumerate(nums):
            s += val
            if s < target:
                continue

            while(s - nums[L] >= target):
                s -= nums[L]
                L += 1
            ans = min(ans, R - L + 1)
            # print("--->ans = ", ans, s, nums[L - 1:R])

            if ans == 1:
                break
        if ans == N + 1:
            return 0
        else:
            return ans

def main():
    A = int(input())
    B = list(map(int, input().split()))
    print(Solution().minSubArrayLen(A, B))

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
