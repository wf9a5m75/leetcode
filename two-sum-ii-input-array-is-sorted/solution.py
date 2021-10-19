import sys
from io import StringIO
from typing import Optional, List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1

        while(L < R):
            s = numbers[L] + numbers[R]
            if (s == target):
                return (L + 1, R + 1)
            elif (s < target):
                L += 1
            else:
                R -= 1



    def binarySearch(self, A, target, L, R):
        while(L != R):
            mid = (L + R) >> 1
            if (A[mid] < target):
                L = mid + 1
            else:
                R = mid
        return L

    def twoSum_with_binarySearch(self, numbers: List[int], target: int) -> List[int]:

        lenNums = len(numbers)
        for i, val in enumerate(numbers):
            expectV = target - val
            if expectV < val:
                # expect = 1 - 9 = -8
                #
                # Since the numbers is sorted in non-decreasing order,
                # -8 is already passed.
                continue

            pos = self.binarySearch(numbers, expectV, i + 1, lenNums)
            if pos == lenNums:
                continue
            if numbers[pos] == expectV:
                return (min(i, pos) + 1, max(i, pos) + 1)
