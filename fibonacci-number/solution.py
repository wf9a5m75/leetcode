class Solution:
    def fib(self, n: int) -> int:
        prevs = [0, 1]
        if n < 2:
            return prevs[n]
        for i in range(2, n + 1):
            prevs[0], prevs[1] = prevs[1], prevs[0] + prevs[1]
        return prevs[1]
        
