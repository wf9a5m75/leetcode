class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        mem = {}
        for char in s:
            mem[char] = mem.get(char, 0) + 1
        for char in t:
            if (char not in mem) or (mem[char] == 0):
                return False
            mem[char] -= 1
        return True
