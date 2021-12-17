class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1 = len(s) - 1
        p2 = len(t) - 1

        skip1 = skip2 = 0
        while(p1 > -1) or (p2 > -1):

            # print(p1, p2)
            if (p1 > -1):
                if s[p1] == "#":
                    skip1 += 1
                    p1 -= 1
                    continue
                elif skip1 > 0:
                    while(skip1 > 0) and (p1 > -1) and (s[p1] != "#"):
                        p1 -= 1
                        skip1 -= 1
                    continue

            if p2 > -1:
                if t[p2] == "#":
                    skip2 += 1
                    p2 -= 1
                    continue
                elif skip2 > 0:
                    while(skip2 > 0) and (p2 > -1) and (t[p2] != "#"):
                        p2 -= 1
                        skip2 -= 1
                    continue

            # Both characters do not match
            if (p1 > -1) and (p2 > -1) and (s[p1] != t[p2]):
                return False

            p1 -= 1
            p2 -= 1
        return (p1 == p2 == -1)
