class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n <= 0):
            return False
        # math.log2(n) returns the number
        # how many times produce 2.
        # So, if n is power of two,
        # the returned number should be integer.
        #
        # Note that math.log(n)/math.log(2) fails when n = 536870912
        p = math.log2(n)

        return p - int(p) == 0
