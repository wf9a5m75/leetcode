class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)

        N = len(arr)
        # We can't spread three equal sum partitions
        if (total % 3 != 0) or (N < 3):
            return False

        oneThird = int(total / 3)

        # Try to find two partions
        s = 0
        cnt = 0
        i = 0
        while(i < N) and (cnt < 3):
            s += arr[i]
            if s == oneThird:
                cnt += 1
                s = 0
            i += 1

        # If we found two partions (cnt == 3),
        # the rest of sum (total - oneThird * 2) should be the same with oneThird
        return (cnt == 3) and (total - oneThird * 2 == oneThird)

"""
test cases
[0,0,0,-1,1]
[0,2,1,-6,6,-7,9,1,2,0,1]
[0,2,1,-6,6,7,9,-1,2,0,1]
[3,3,6,5,-2,2,5,1,-9,4]
[18,12,-18,18,-19,-1,10,10]
[1,-1,1,-1]
[0,0,1,-1]
[-1,0,0,1]
[1,1,1,-1,-1,1,-1,0,-1,-1,-1,1,1,1,0,0,0,0]
"""
