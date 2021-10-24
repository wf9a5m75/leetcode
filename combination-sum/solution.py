import sys
from io import StringIO
from typing import List

class Solution:
    def __init__(self):
        self.visited = set()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        stack = [(target, [])]
        while(stack):
            target, path = stack.pop()
            path.sort()
            key = str(path)
            if key not in self.visited:
                self.visited.add(key)
            else:
                continue

            for val in candidates:
                s = target - val
                if (s > 0):
                    nextPath = path.copy()
                    nextPath.append(val)
                    stack.append((s, nextPath))
                elif (s == 0):
                    nextPath = path.copy()
                    nextPath.append(val)
                    nextPath.sort()
                    key = str(nextPath)
                    if key not in self.visited:
                        self.visited.add(key)
                        results.append(nextPath)
        return results




def main():
    n, target = list(map(int, input().split()))
    A = list(map(int, input().split()))
    results = Solution().combinationSum(A, target)
    print(len(results))
    for result in results:
        print(*result)

def test(testName, inputFile, outputFile):
    capture = StringIO()
    sys.stdin = open(inputFile)
    sys.stdout = capture
    main()
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__
    results = capture.getvalue().split("\n")


    fAnsFile = open(outputFile)
    ansLines = list(map(lambda x: x.strip(), list(fAnsFile)))
    results = list(map(lambda x: x.strip(), results))
    nAns = int(ansLines.pop(0))
    nResults = int(results.pop(0))
    passTheTest = nAns == nResults

    answerSet = set(ansLines)
    for i in range(nResults):
        if results[i] in answerSet:
            results[i] = "   |" + results[i]
        else:
            results[i] = "-->|" + results[i]

    if ((not passTheTest)):
        print("[{0}] -> fail".format(testName))
        print("\n".join(results))
    else:
        print("[{0}] -> pass".format(testName))

    fAnsFile.close()
    capture.close()


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
    # test5()
    # test6()
    # test7()
    # test8()
    # test9()
