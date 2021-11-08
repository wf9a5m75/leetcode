class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xXORy = x ^ y
        d = 0
        while(xXORy > 0):
            if (xXORy & 1) != 0:
                d += 1
            xXORy >>= 1
        return d
