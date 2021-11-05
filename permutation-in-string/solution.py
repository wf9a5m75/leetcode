from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (s1 == s2):
            return True

        N1, N2 = len(s1), len(s2)
        L, R = 0, N1 - 1

        s1counts = Counter(s1)
        substrCounts = Counter(s2[:N1])
        s2 += "$$"
        while(R <= N2):
            # print(s2[L:R], substrCounts, L, R)
            diffCounts = s1counts - substrCounts
            if len(diffCounts) == 0:
                return True

            substrCounts[s2[L]] -= 1
            R += 1
            L += 1
            substrCounts[s2[R]] += 1
        return False
