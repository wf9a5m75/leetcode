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



    results.append(test("test1", func,
        "leetcode",
        ["leet","code"],
        expectResult = True))
    results.append(test("test2", func,
        "applepenapple",
        ["apple","pen"],
        expectResult = True))
    results.append(test("test3", func,
        "catsandog",
        ["cats","dog","sand","and","cat"],
        expectResult = False))
    results.append(test("test4", func,
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"],
        expectResult = False))
    # results.append(test("test7", func,
    #     [["a","b"],["a","a"]],
    #     ["aba","baa","bab","aaab","aaa","aaaa","aaba"],
    #     expectResult = ["aba","aaa","aaab","baa","aaba"]))
    total = 0
    for result in results:
        total += result[0]
        print(result)
    print("total = {}μs".format(total))
