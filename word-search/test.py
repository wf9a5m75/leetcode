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
    results.append(test("test1", func, [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", expectResult = True))
    results.append(test("test2", func, [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", expectResult = True))
    results.append(test("test3", func, [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", expectResult = False))
    results.append(test("test4", func, [["b"],["a"],["b"],["b"],["a"]], "baa", expectResult = False))
    results.append(test("test5", func, [["A","Z","A","A"],["A","B","B","B"],["A","C","B","B"],["A","B","B","B"],["A","B","B","B"]], "BBBBBBBCBZ", expectResult = True))
    results.append(test("test6", func, [["a","a","b","a","a","b"],["a","a","b","b","b","a"],["a","a","a","a","b","a"],["b","a","b","b","a","b"],["a","b","b","a","b","a"],["b","a","a","a","a","b"]], "bbbaabbbbbab", expectResult = False))
    results.append(test("test7", func, [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS", expectResult = True))
    total = 0
    for result in results:
        total += result[0]
        print(result)
    print("total = {}μs".format(total))
