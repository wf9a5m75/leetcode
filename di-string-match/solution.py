class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        D = len(s)
        I = 0
        results = []
        for c in s:
            if c == "I":
                results.append(I)
                I += 1
            else:
                results.append(D)
                D -= 1
        results.append(I)
        return results
