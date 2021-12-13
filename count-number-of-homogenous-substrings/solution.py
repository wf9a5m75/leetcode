class Solution:
    def __init__(self):
        self.MOD = 1000000007
        self.mem = {
            0: 0,
            1 : 1
        }

    def summution(self, n):
        if n in self.mem:
            return self.mem[n]
        n %= self.MOD
        self.mem[n] = (n * (n + 1)) >> 1
        return self.mem[n]

    def countHomogenous(self, s: str) -> int:
        ans = 0
        prevChar = ""
        prevCnt = 0
        s += "$"
        for char in s:
            if char != prevChar:
                ans = (ans + self.summution(prevCnt)) % self.MOD
                prevCnt = 0
            prevChar = char
            prevCnt += 1
        return ans
