class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #
        # DP + backtracking approach
        #
        chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        N = len(digits)
        if (N == 0):
            return []

        def recursive(prev: List[str], idx: int) -> List[str]:
            if (idx == N):
                return prev

            results = []
            for char in chars[digits[idx]]:
                for i in range(len(prev)):
                    results.append(prev[i] + char)
            return recursive(results, idx + 1)
        return recursive([""], 0)
