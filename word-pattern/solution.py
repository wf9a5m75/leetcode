class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) !=  len(pattern):
            return False
        PtoS = {}
        StoP = {}
        for i in range(len(pattern)):
            cur_letter = pattern[i]
            cur_word = s[i]
            if cur_letter not in PtoS and cur_word not in StoP:
                PtoS[cur_letter] = cur_word
                StoP[cur_word] = cur_letter
            elif PtoS.get(cur_letter) != cur_word or StoP.get(cur_word) != cur_letter:
                return False
        return True
