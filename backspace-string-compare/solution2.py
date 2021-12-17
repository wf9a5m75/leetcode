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
