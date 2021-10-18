import sys
from io import StringIO
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 1 2 3 3
        #     A
        #   B
        #-----
        # 1 2 2 3 3
        #       A
        #     B
        #-----
        # 1 2 3 3 3
        #          A
        #     B
        A = head
        B = head
        while(A is not None):
            if A.val == B.val:
                A = A.next
            else:
                B = B.next
                B.val = A.val
        # wow, head is None ...
        if B is not None:
            B.next = None
        return head

def main():
    A = list(map(int, input().split()))
    root = ListNode(A[0])
    curr = root
    for i in range(1, len(A)):
        node = ListNode(A[i])
        curr.next = node
        curr = node

    result = Solution().deleteDuplicates(root)

    answer = []
    while(result is not None):
        answer.append(result.val)
        result = result.next
    print(*answer)

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


def test1():
    test("test1", "input01.txt", "output01.txt")

def test0():
    test("test0", "input00.txt", "output00.txt")

if __name__ == "__main__":
    test0()
    test1()
