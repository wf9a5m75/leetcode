# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        L = 1
        R = n
        while(L != R):
            mid = (L + R) >> 1
            rc = guess(mid)
            if (rc == 0):
                return mid
            elif rc == -1:
                R = mid - 1
            else:
                L = mid + 1
        return L
