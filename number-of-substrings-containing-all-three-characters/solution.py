class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        ans = 0
        counts = {"a": 0, "b": 0, "c": 0}

        L = R = 0
        counts[s[0]] += 1
        while(R < N):
            hasAll = (counts["a"] > 0) and (counts["b"] > 0) and (counts["c"] > 0)
            if hasAll:
                ans += (N - R)
                counts[s[L]] -= 1
                L += 1
            else:
                R += 1
                if (R < N):
                    counts[s[R]] += 1
        return ans
