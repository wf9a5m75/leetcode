class Solution:
    def addDigits(self, num: int) -> int:
        while(num > 9):
            ans = 0
            while(num > 0):
                ans += (num % 10)
                num //= 10
            num = ans
        return num
