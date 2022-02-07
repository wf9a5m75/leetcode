class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sSet = Counter(s)
        tSet = Counter(t)

        for key in t:
            if (key not in sSet) or (sSet[key] != tSet[key]):
                return key
