class Solution_works_only_non_negative_integers:
    def getSum(self, a: int, b: int) -> int:
        ans = 0
        carryUp = 0
        i = 0
        while(a > 0) or (b > 0) or (carryUp > 0):
            s = (carryUp << 2) | ((a & 1) << 1) | (b & 1)
            a <<= 1
            b <<= 1
            """
            s = [000, 001, 010, 011, 100, 101, 110, 111]
            """
            carryUp = 0
            if (s == 3) or (s > 4):
                carry = 1
            if s == 1 or s == 2 or s == 4 or s == 7:
                ans += 2**i
            i += 1
        return ans

import math
class Solution:
    def getSum(self, a: int, b: int) -> int:

        #
        # This idea is smart!
        # https://leetcode.com/problems/sum-of-two-integers/discuss/1512422/Simple-solution-using-Exponents-and-Log-%3A-faster-then-92
        #
        fact1 = math.pow(2, a)
        fact2 = math.pow(2, b)
        prod = fact1 * fact2
        ans = math.log2(prod)
        return int(ans)
