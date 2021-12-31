class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        #
        # L = 5, R = 12
        #
        # 12 & 11 => 1000b
        # (skip 10,9)
        # 8 & 7 => 0000b (stop)
        num = right
        while(num > left):
            num = num & num - 1
        return num & left
            
