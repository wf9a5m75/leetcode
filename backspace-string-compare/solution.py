class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1 = len(s) - 1
        p2 = len(t) - 1
        skip1 = skip2 = 0
        while(p1 >= 0) or (p2 >= 0):
            while(p1 >= 0):
                if s[p1] == "#":
                    skip1 += 1
                    p1 -= 1
                elif skip1 > 0:
                    skip1 -= 1
                    p1 -= 1
                else:
                    break

            while(p2 >= 0):
                if t[p2] == "#":
                    skip2 += 1
                    p2 -= 1
                elif skip2 > 0:
                    skip2 -= 1
                    p2 -= 1
                else:
                    break

            if (p1 == -1) and (p2 == -1):
                break

            if (p1 == -1) or (p2 == -1):
                return False
            if (s[p1] == t[p2]):
                p1 -= 1
                p2 -= 1
            else:
                return False

        return True

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

    def backspaceCompare2(self, s: str, t: str) -> bool:

        return self.buildString(s) == self.buildString(t)
