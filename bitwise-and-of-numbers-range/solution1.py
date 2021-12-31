class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Because AND of all numbers,
        # if the numbers are not same, last digit must be 0.
        # So just need to record how many shifts we did
        shift = 0
        while(left != right):
            left >>= 1
            right >>= 1
            shift+=1
        return left << shift
