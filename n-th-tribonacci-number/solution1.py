class Solution:
    def tribonacci(self, n: int) -> int:
        mem = {
            0: 0,
            1: 1,
            2: 1
        }
        for i in range(0, n - 2):
            mem[i + 3] = mem[i] + mem[i + 1] + mem[i + 2]
        return mem[n]
