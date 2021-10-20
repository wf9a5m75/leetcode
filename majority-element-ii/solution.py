import sys
from io import StringIO
from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # heap sort approach
        frequencies = Counter(nums)

        # Obtains top 2 (because we are looking for n / 3)
        top2 = heapq.nlargest(2, frequencies, key=frequencies.get)

        # Filtering
        threshold = n / 3
        results = list(filter(lambda element: frequencies[element] > threshold, top2))

        return results

    def majorityElement_moor_voting(self, nums: List[int]) -> List[int]:
        n = len(nums)
        majorities = [nums[0], 10**9 + 1] # 10**9 + 1 never meet in the array
        counts = [1, 0]
        for i in range(1, n):
            val = nums[i]
            if val == majorities[0]:
                counts[0] += 1
            elif val == majorities[1]:
                counts[1] += 1
            elif counts[0] == 0:
                majorities[0] = val
                counts[0] = 1
            elif counts[1] == 0:
                majorities[1] = val
                counts[1] = 1
            else:
                counts[0] -= 1
                counts[1] -= 1

        counts = [0, 0]
        for val in nums:
            counts[0] += bool(majorities[0] == val)
            counts[1] += bool(majorities[1] == val)
        print(*majorities)
        print(*counts)

        threshold = n / 3
        results = []
        for i in range(2):
            if counts[i] > threshold:
                results.append(majorities[i])
        return results


def main():
    A = list(map(int, input().strip().split()))
    results = Solution().majorityElement(A)
    print(*results)

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
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()
    # test8()
