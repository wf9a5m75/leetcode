from functools import cmp_to_key

class Solution:
    def frequencySort(self, s: str) -> str:
        mem = {}
        for char in s:
            mem[char] = mem.get(char, 0) + 1
        s = ''

        counts = []
        for char in mem:
            counts.append((char, mem[char]))
        mem = None

        counts.sort(key = lambda x: x[1])

        i = len(counts) - 1
        while (i >= 0) and (counts[i][1] > 0):
            s += (counts[i][0] * counts[i][1])
            i -=1
        return s
