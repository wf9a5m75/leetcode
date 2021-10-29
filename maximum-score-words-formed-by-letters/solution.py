from collections import Counter

class Solution:

    def backtracking(self,
                     words: List[str],
                     letterCounts: Counter,
                     scoreTable: Mapping[str, int],
                     soFarScore: int,
                     path: List[str] = []
                    ) -> int:

        # If the words list is empty,
        # we tried all combination.
        # Return the score
        if (len(words) == 0):
            print(soFarScore, path)
            return soFarScore

        # Get one word
        word = words.pop(0)

        # Calculate the score if we don't include the word
        score1 = self.backtracking(words.copy(),
                                    letterCounts.copy(),
                                    scoreTable,
                                    soFarScore,
                                   path.copy()
                                  )

        # Calculate the score if the word can be consisted using remained letters
        score2 = 0
        canBeConsisted = True
        for w in word:
            letterCounts[w] -= 1
            if letterCounts[w] < 0:
                canBeConsisted = False
                break
            score2 += scoreTable[w]

        if canBeConsisted:
            # If the word can be consisted using remained letters,
            # continue the process.
            # Otherwise, stop the process
            path.append(word)
            soFarScore = self.backtracking(words,
                                           letterCounts,
                                           scoreTable,
                                           soFarScore + score2,
                                            path
                                          )

        # Return the higher score, include the word or not.
        return max(soFarScore, score1)

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        # Count up each characters
        letterCounts = Counter(letters)

        # Convert score array to score table
        scoreTable = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i, char in enumerate(alphabet):
            scoreTable[char] = score[i]

        # Calculate the maximum score
        maxScore = self.backtracking(words, letterCounts, scoreTable, 0)

        return maxScore
