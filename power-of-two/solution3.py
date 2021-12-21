class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        #
        # example: n = 10
        #
        # n(binary)     = 1010
        # n - 1(binary) = 1001
        #            ---------
        #                 1000
        #
        # ======================
        #
        # example: n = 16
        #
        # n(binary)     = 10000
        # n - 1(binary) = 01111
        #               -------
        #                 00000

        return (n & (n - 1)) == 0
