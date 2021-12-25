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

def test(caseName, func, *args, expectResult):
    result = measure(func)(*args)

    testResult = "pass" if result[1] == expectResult else "fail"
    return [result[0], caseName, testResult, result[1]]


def checkTests(func):
    results = []
    results.append(test("test1", func, " 3 / 2", expectResult = 1))
    results.append(test("test2", func, " 4 +  3*5 / 2 * 4 / 5 - 10", expectResult = -1))
    total = 0
    for result in results:
        total += result[0]
        print(result)
    print("total = {}μs".format(total))
