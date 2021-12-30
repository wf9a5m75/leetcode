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

    result[1].sort()
    expectResult.sort()
    testResult = "pass" if result[1] == expectResult else "fail"
    return [result[0], caseName, testResult, result[1]]






def checkTests(func):
    results = []



    results.append(test("test1", func,
        [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
        ["oath","pea","eat","rain"],
        expectResult = ["oath","eat"]))
    results.append(test("test2", func,
        [["a","b"],["c","d"]],
        ["abcb"],
        expectResult = []))
    results.append(test("test3", func,
        [["a","b","c"],["a","e","d"],["a","f","g"]],
        ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"],
        expectResult = ["abcdefg","gfedcbaaa","eaabcdgfa","befa"]))
    results.append(test("test4", func,
        [["h","e","l","l","o","x","w","o","r","l","d","p"],["p","r","o","g","r","a","m","i","g","u","i","s"],["f","f","f","l","a","g","n","p","e","n","p","f"],["a","a","p","p","m","m","e","h","o","a","t","u"],["m","m","e","l","r","a","m","o","p","p","p","n"],["i","l","y","b","a","t","t","n","g","i","z","n"],["a","b","a","a","c","t","d","o","o","o","a","y"],["n","a","b","n","a","t","m","a","o","n","s","u"],["n","n","n","a","b","t","r","r","o","i","s","n"]],
        ["fun","funny","frog","grammar","ramen","rumen","iphone","game","guinapig","banana"],
        expectResult = ["fun","funny","frog","grammar","ramen"]))
    results.append(test("test5", func,
        [["a"]],
        ["ab"],
        expectResult = []))
    results.append(test("test6", func,
        [["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]],
        ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"],
        expectResult = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
    results.append(test("test7", func,
        [["a","b"],["a","a"]],
        ["aba","baa","bab","aaab","aaa","aaaa","aaba"],
        expectResult = ["aba","aaa","aaab","baa","aaba"]))
    total = 0
    for result in results:
        total += result[0]
        print(result)
    print("total = {}μs".format(total))
