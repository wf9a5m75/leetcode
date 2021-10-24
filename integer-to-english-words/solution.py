import sys
from io import StringIO
from typing import List

class Solution:
    def numberToWords(self, num: int) -> str:
        engNumDic = {
            "1" : "One",
            "2" : "Two",
            "3" : "Three",
            "4" : "Four",
            "5" : "Five",
            "6" : "Six",
            "7" : "Seven",
            "8" : "Eight",
            "9" : "Nine",
            "10" : "Ten",
            "11" : "Eleven",
            "12" : "Twelve",
            "13" : "Thirteen",
            "14" : "Fourteen",
            "15" : "Fifteen",
            "16" : "Sixteen",
            "17" : "Seventeen",
            "18" : "Eighteen",
            "19" : "Nineteen",
            "20" : "Twenty",
            "30" : "Thirty",
            "40" : "Forty",
            "50" : "Fifty",
            "60" : "Sixty",
            "70" : "Seventy",
            "80" : "Eighty",
            "90" : "Ninety",
            "100" : "Hundred",
            "1000" : "Thousand",
            "1000000" : "Million",
            "1000000000" : "Billion"
        }
        if num == 0:
            return "Zero"


        def convertToEnglish(num):
            result = []
            # Billion -> Million -> Thousand -> Hundred
            for base in [1000000000, 1000000, 1000, 100]:
                if (num >= base):
                    # print(num, base)
                    d = num // base
                    if (d > 9):
                        result += convertToEnglish(d) + [engNumDic[str(base)]]
                        num -= d * base
                    else:
                        result.append(engNumDic[str(d)])
                        result.append(engNumDic[str(base)])
                        num -= d * base
                # print(" ---> ", result)

            if (num > 0):
                if (num <= 20) or (num % 10 == 0):
                    result.append(engNumDic[str(num)])
                else:
                    d = num // 10
                    result.append(engNumDic[str(d * 10)])
                    result.append(engNumDic[str(num % 10)])
                # print(" ---> ", result)
            return result
        result = convertToEnglish(num)

        return " ".join(result)

def main():
    A = int(input())
    print(Solution().numberToWords(A))

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
    test5()
    test6()
    test7()
    test8()
    test9()
