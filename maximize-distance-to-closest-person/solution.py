class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        #
        # O(N) time
        # O(1) space
        # https://leetcode.com/problems/maximize-distance-to-closest-person/discuss/1692673/Python-or-one-pass-or-O(N)-time-O(1)-space
        #
        firstEmpty = -1
        lastEmpty = 0
        emptyCnt = 0
        maxEmptyCnt = 0
        for seat in seats:

            # Find the largest consective number of empty seats
            if seat == 0:
                emptyCnt += 1
            else:
                if firstEmpty == -1:
                    firstEmpty = emptyCnt
                lastEmpty = emptyCnt

                maxEmptyCnt = max(maxEmptyCnt, emptyCnt)

                emptyCnt = 0

        # If the seats[0] is empty, we also check the firstEmpty.
        # Otherwise, we don't use it
        if seats[0] == 1:
            firstEmpty = -1


        # If the seats[-1] is empty, we also check the lastEmpty.
        # Otherwise, we don't use it
        if seats[-1] == 1:
            lastEmpty = -1

        # Return the maximum distance
        return max(firstEmpty, lastEmpty, math.ceil(maxEmptyCnt / 2))
