class Solution:
    def countSegments(self, s: str) -> int:
        ans = 0
        hasCharacterBefore = False

        for c in s:
            if (hasCharacterBefore == False):
                if (c != " "):
                    ans += 1
                    hasCharacterBefore = True
            elif c == " ":
                hasCharacterBefore = False
        return ans
