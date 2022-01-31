class Solution:
    def numSplits(self, s: str) -> int:
        N = len(s)
        prefixSet = set()
        suffixSet = set()
        prefix = [0] * N
        suffix = [0] * N

        ordA = ord('a')
        for L in range(N):
            prefixSet.add(s[L])
            prefix[L] = len(prefixSet)

            suffixSet.add(s[N - 1 - L])
            suffix[N - 1 - L] = len(suffixSet)

        ans = 0
        for L in range(N - 1):
            if prefix[L] == suffix[L + 1]:
                ans += 1
        return ans
