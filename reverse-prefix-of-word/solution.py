class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        # 1. Find the ch
        L = R = 0
        N = len(word)
        while(R < N) and (word[R] != ch):
            R += 1

        # 2. Reverse the word
        while(R < N) and (L < R):
            word[L], word[R] = word[R], word[L]
            L += 1
            R -= 1

        return "".join(word)
