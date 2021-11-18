class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        """
        Optimized solution
        """
        orgK = k
        N = len(answerKey)
        L = 0
        for char in answerKey:
            if char == "T":
                k -= 1
            if k < 0:
                if answerKey[L] == "T":
                    k += 1
                L += 1
        falseCount = N - L


        L = 0
        k = orgK
        for char in answerKey:
            if char == "F":
                k -= 1
            if k < 0:
                if answerKey[L] == "F":
                    k += 1
                L += 1
        trueCount = N - L

        return max(falseCount, trueCount)

    def _maxConsecutive(self, answerKey: str, k: int, correct: str, incorrect: str) -> int:
        N = len(answerKey)
        L = R = ans = 0

        while(R < N):
            if (answerKey[R] == correct):
                if (k > 0):
                    k -= 1
                    R += 1
                else:
                    ans = max(ans, R - L)
                    while(answerKey[L] == incorrect):
                        L += 1
                    L += 1
                    k += 1
            else:
                R += 1
        ans = max(ans, R - L)
        return ans

    def maxConsecutiveAnswers_myanswer(self, answerKey: str, k: int) -> int:
        ans = self._maxConsecutive(answerKey, k, "T", "F")
        ans = max(ans, self._maxConsecutive(answerKey, k, "F", "T"))

        return ans
