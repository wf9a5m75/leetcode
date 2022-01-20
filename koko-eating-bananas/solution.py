class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = 10**9
        N = len(piles)
        while(L != R):
            mid = (L + R) >> 1

            hour_spent = 0
            for pile in piles:
                hour_spent += math.ceil(pile / mid)


            if (hour_spent <= h):
                R = mid
            else:
                L = mid + 1
        return L
