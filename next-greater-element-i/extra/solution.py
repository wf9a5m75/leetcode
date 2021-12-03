import time
from typing import List

def measure(func):
    def wrapper(*args, **kargs):
        start_time = time.perf_counter()

        result = func(*args, **kargs)

        end_time = time.perf_counter()
        execution_time = end_time - start_time
        return [int(execution_time * 1000 * 1000), result]
        # print(f'{func.__name__}: {execution_time}')
        # return result
    return wrapper

def test(caseName, func, nums, expectResult):
    result = measure(func)(nums)
    testResult = "pass" if result[1] == expectResult else "fail"
    return [result[0], caseName, testResult, result[1]]

def checkTests(func):
    results = []
    results.append(test("test1", func, [1,2,1,2,3], [2,3,2,3,-1]))
    results.append(test("test2", func, [52,62,61,60,53,54,53,54,57,56,62,65,64], [62, 65, 62, 62, 54, 57, 54, 57, 62, 62, 65, -1, -1]))
    results.append(test("test3", func, [5,4,3,5,4,3], [-1,5,5,-1,-1,-1]))
    results.append(test("test4", func, [0], [-1]))
    results.append(test("test5", func, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,-1]))
    total = 0
    for result in results:
        total += result[0]
        print(result)
    print("total = {}μs".format(total))

def nextGreaterValueII(nums: List[int]) -> List[int]:
    stack = []
    result = []
    for num in reversed(nums):
        while(stack) and (num >= stack[-1]):
            stack.pop()
        if (stack):
            result.insert(0, stack[-1])
        else:
            result.insert(0, -1)
        stack.append(num)
    return result

checkTests(nextGreaterValueII)
