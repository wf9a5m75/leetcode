from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countsDic = Counter(magazine)
        for r in ransomNote:
            if (r not in countsDic) or (countsDic[r] == 0):
                return False
            countsDic[r] -= 1
        return True
