class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        A=[]
        val = x
        while(val > 0):
            A.append(val % 10)
            val = val // 10

        val = 0
        for a in A:
            val = val * 10 + a
        return val == x
