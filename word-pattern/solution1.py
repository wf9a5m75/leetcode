class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # Separates "s" by spacing
        #
        # This problem guarantees no-leading or trailing spaces,
        # and all the words in s are separated by a single space.
        # So, s.split(" ") is enough.
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        pattern_to_word = {}
        word_to_pattern = {}

        for i in range(len(pattern)):
            p = pattern[i]
            word = words[i]

            # If the pattern char is not registered,
            # we check the `word` side.
            if p not in pattern_to_word:

                # If the word is bounded to another pattern,
                # return false
                if word in word_to_pattern:
                    return False

                # Regists the p and the word.
                pattern_to_word[p] = word
                word_to_pattern[word] = p

            # The word should be bounded to the p,
            # and the p should be bounded to the word.
            # If either one is incorrect, return False
            elif (pattern_to_word[p] != word) or (word_to_pattern[word] != p):
                return False
        return True
        
