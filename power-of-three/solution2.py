import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if (n <= 0):
            return False

        # Do not use math.log(n)/math.log(3)
        # math.log10() is more accurate than math.log()

        p = math.log10(n) / math.log10(3)
        p = ((p * 1000) / 1000)
        return p - int(p) == 0
