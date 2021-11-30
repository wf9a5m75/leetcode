class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1 = p2 = 0
        N1, N2 = len(name), len(typed)
        while(p1 < N1) and (p2 < N2):
            if (name[p1] == typed[p2]):
                p2 += 1
                p1 += 1
            elif (p1 > 0) and (name[p1 - 1] == typed[p2]):
                p2 += 1
            else:
                return False
        if (p2 < N2):
            while(p2 < N2) and (typed[p2] == name[p1 - 1]):
                p2 += 1
        return (p1 == N1) and (p2 == N2)
