class Solution:
    def buildString(self, s: str) -> int:
        result = []
        i = len(s) - 1
        skip = 0
        while(i >= 0):
            if (skip == 0):
                while(i >= 0) and (s[i] != "#"):
                    result.append(s[i])
                    i -= 1
            else:
                while(i >= 0) and (skip > 0) and (s[i] != "#"):
                    i -= 1
                    skip -= 1

            if (i >= 0) and (s[i] == "#"):
                i -= 1
                skip += 1
        return "".join(result)

    def backspaceCompare(self, s: str, t: str) -> bool:

        return self.buildString(s) == self.buildString(t)
