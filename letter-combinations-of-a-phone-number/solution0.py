class Solution:
    def __init__(self):
        self.digitToChars =[
            ["0"],
            ["1"],
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"],
            ["j", "k", "l"],
            ["m", "n", "o"],
            ["p", "q", "r", "s"],
            ["t", "u", "v"],
            ["w", "x", "y", "z"]
        ]
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if (n == 0):
            return []

        chars = self.digitToChars[int(digits[0])]
        if (n == 1):
            return chars

        results = []
        others = []
        if (n > 1):
            others = self.letterCombinations(digits[1:])

        for char in chars:
            for other in others:
                results.append(char + other)
        return results
        
