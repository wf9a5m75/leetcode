class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        L = 0
        R = int(num ** 0.5)

        while(L != R):
            mid = (L + R) >> 1
            if mid * mid == num:
                return True
            elif mid < num:
                L = mid + 1
            else:
                R = mid
        return (L * L == num)
