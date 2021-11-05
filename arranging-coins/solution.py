class Solution:
    def arrangeCoins(self, n: int) -> int:
        L = 0
        R = n
        while(L <= R):
            rows = (L + R) >> 1

            s = (rows * (rows + 1)) >> 1
            if (s == n):
                return rows
            elif (s < n):
                L = rows + 1
            else:
                R = rows - 1
        return R



    def arrangeCoins_slow(self, n: int) -> int:
        rows = 0
        s = 0
        while(((rows * (rows + 1)) >> 1) <= n):
            rows += 1
        rows -= 1
        return rows

            
