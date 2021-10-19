# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        L = 1
        R = n
        while(L != R):
            mid = (L + R) >> 1
            if isBadVersion(mid):
                R = mid
            else:
                L = mid + 1

        return L
