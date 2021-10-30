class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        # Need to know about the Gray code
        # https://en.wikipedia.org/wiki/Gray_code
        arrSize = 2**n
        p = [0] * arrSize

        for i in range( arrSize):
            p[i] = i ^ (i >> 1)

        startIdx = p.index(start)
        return p[startIdx:] + p[:startIdx]
    
