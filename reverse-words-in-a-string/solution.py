class Solution:
    def reverseStrInRange(self, s: List[str], L: int, R: int) -> None:
        while(L < R):
            s[L], s[R] = s[R], s[L]
            L += 1
            R -= 1

    def reverseWords(self, s: str) -> str:
        s = list(s)
        N = len(s)

        # Reverse the word overall
        self.reverseStrInRange(s, 0, N - 1)

        # Reverse each word
        L = R = 0
        while(R < N):
            while(R < N) and (s[R] != " "):
                R += 1
            self.reverseStrInRange(s, L, R - 1)

            L = R = R + 1

        # Shift back  unnecessary spaces
        nonSpaceIdx = 0
        spaceIdx = 0
        while(nonSpaceIdx < N):
            while(nonSpaceIdx < N) and (s[nonSpaceIdx] == " "):
                nonSpaceIdx += 1

            while(nonSpaceIdx < N) and (s[nonSpaceIdx] != " "):
                s[spaceIdx], s[nonSpaceIdx] = s[nonSpaceIdx], s[spaceIdx]
                spaceIdx += 1
                nonSpaceIdx += 1
            if (spaceIdx < N):
                s[spaceIdx] = " "
                spaceIdx += 1


        # Trim unnecessary spaces
        spaceIdx = min(spaceIdx, N - 1)
        while(spaceIdx > 0) and (s[spaceIdx] == " "):
            spaceIdx -= 1
        N = spaceIdx + 1
        s = s[:N]

        # join
        return "".join(s)
