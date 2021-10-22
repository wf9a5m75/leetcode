class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        sizeA = len(A)
        sizeB = len(B)
        if (sizeA > sizeB):
            return self.findMedianSortedArrays(B, A)

        L = 0
        R = sizeA

        A_and_B_mid = (sizeA + sizeB + 1) // 2

        while(L <= R):
            mid1 = (L + R) // 2
            mid2 = A_and_B_mid - mid1
            # print(mid1, mid2)

            maxLeftA = float("-inf") if mid1 == 0 else A[mid1 - 1]
            minRightA = float("inf") if mid1 == sizeA else A[mid1]
            maxLeftB = float("-inf") if mid2 == 0 else B[mid2 - 1]
            minRightB = float("inf") if mid2 == sizeB else B[mid2]

            if (maxLeftA <= minRightB) and (maxLeftB <= minRightA):
                # A = 1 3  8 9  | 15
                #               └----┐
                # B =     7   11     | 18 19 21 25
                #
                # maxLeftA (9) <= minRightB (18)  -> True
                # maxLeftB (11) <= minRightA (15)  -> True
                #
                if (sizeA + sizeB) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                else:
                    return float(max(maxLeftA, maxLeftB))
            elif maxLeftB > minRightA:
                # A = 1 3   | 8 9   15 |
                #           └----------------┐
                # B =     7       11   18 19 | 21 25
                #
                # maxLeftA (3) <= minRightB (21)  -> True
                # maxLeftB (19) <= minRightA (8)  -> False
                #
                # Then the separator in B should be more left.
                # So, the separator in A should be more right.
                L = mid1 + 1
            else:
                # A = 1 3     8 9   15 |
                #         ┌------------┘
                # B =     | 7     11   18 19 21 25
                #
                # maxLeftA (INF) <= minLeftB (11)  -> False
                # maxLeftB (-INF) <= minLeftA (15)  -> True
                #
                # Then the separator in B should be more right.
                # So, the separator in A should be more left.

                R = mid1 - 1
