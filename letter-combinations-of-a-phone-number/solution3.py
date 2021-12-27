class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #
        # DP approach
        #
        if (digits):
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
            currS = [""]
            for d in digits:
                currS = [prev + c for prev in currS for c in chars[d]]
            return currS
        return []
