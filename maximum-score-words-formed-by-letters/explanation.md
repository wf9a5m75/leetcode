First, I took a time a little to understand this question.
Let me explain with an example.

```
words  = ["xxxz",  "ax",  "bx",  "cx"]
letters = ["z",  "a",  "b",  "c",  "x",  "x",  "x"]
score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]

-------------

The question says "If we choose one word using letters, can we make another word using the remained letters?"

(preparation)
letters = ( a = 1, b = 1, c = 1, x = 3, z = 1 )
scores = ( a = 4, b = 4, c = 4, x = 5 ,z = 10 )

----------------------------------------------------------------
Case1

step1 ) start "xxxz"

  Since this word uses "three x" and "one z", the remaining letters become,
    letters = (a = 1, b = 1, c = 1, x = 0, z= 0)
  and score becomes,
    score = score[x] * 3 + score[z] * 1 = 5 * 3 + 1 * 10 = 25

 Move on to the next word

step 2 ) "ax"

  At this time, can we make "ax" using remained letters? -> No.
  Because "x" is out of stock.
 That's why ["xxxz"] 's score is 27

----------------------------------------------------------------

Case 2

step1 ) start "ax"
   We spend "one a" and "one x", so remaining letters are
      letters = ( a = 0, b = 1, c = 1, x = 2, z = 1 )
   and score is
      score = score[a] * 1 + score[x] * 1 = 4 + 5 = 9

   Move on to the next word

-----
step2 ) "bx"
   We spend "one b" and "one x", so remaining letters are
      letters = ( a = 0, b = 0, c = 1, x = 1, z = 1 )
   and score is
      score = score[b] * 1 + score[x] * 1 = 4 + 5 = 9
	  soFarScore = soFarScore + score = 9 + 9 = 18

   Move on to the next word
-----
step3 ) "cx"
   We spend "one c" and "one x", so remaining letters are
      letters = ( a = 0, b = 0, c = 0, x = 1, z = 1 )
   and score is
      score = score[c] * 1 + score[x] * 1 = 4 + 5 = 9
	  soFarScore = soFarScore + score = 18 + 9 = 27

   Move on to the next word

-----
step4 ) "xxxz"
   At this time, we can not make "xxxz" because "x" is not enough.
   That's why ["ax", "bx", "cx"] 's score is 27

```

As you can see the above example, we need to try all combinations, if we choose the word or not.

Actually, you can approach using DP as well. But the below code is backtracking.

```python
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
```
