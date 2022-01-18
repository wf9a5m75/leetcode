class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if (n == 0):
            return True

        # left side of the flowerbed[0] is empty.
        # so zeroCnt = 1
        zeroCnt = 1
        for spot in flowerbed:
            if spot == 0:
                zeroCnt = zeroCnt + 1

                # if three 0 consective, we can put a flower in the middle.
                if zeroCnt == 3:
                    n -= 1
                    zeroCnt = 1

                    # All done, return true
                    if n == 0:
                        return True
            else:
                zeroCnt = 0

        # Lastly, on the right edge, there is no flower.
        # so, if one flower is left, and so far zeroCnt = 2, we can put a flower.
        return (n == 1) and (zeroCnt == 2)
