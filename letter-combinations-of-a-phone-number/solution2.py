class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #
        # DP approach
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

        currS = [""]
        for d in digits:
            nextS = []
            for prev in currS:
                for c in chars[d]:
                    nextS.append(prev + c)
            currS = nextS
        return currS
