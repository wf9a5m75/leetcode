class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pDict = Counter(p)
        pDict["another"] = 0
        wDict = {
            "another": 0
        }

        s += "$"
        N = len(s)
        L = R = 0
        pSize = len(p)
        results = []
        while(R < N):
            char = s[R]
            if (R - L < pSize):
                R += 1
                if char in pDict:
                    wDict[char] = wDict.get(char, 0) + 1
                else:
                    wDict["another"] += 1
            else:
                matched = True
                for wKey in wDict:
                    if pDict.get(wKey) != wDict[wKey]:
                        matched = False
                        break
                if matched:
                    results.append(L)

                if s[L] in pDict:
                    wDict[s[L]] -= 1
                else:
                    wDict["another"] -= 1
                L += 1
        return results
                    
