class Solution:
    def isUgly(self, n: int) -> bool:
        if (n < 1):
            return False
        if (n == 1):
            return True
        while(n > 1):
            if (n % 5 == 0):
                n /= 5
            elif (n % 3 == 0):
                n /= 3
            elif (n % 2 == 0):
                n /= 2
            else:
                return False
        return n == 1
