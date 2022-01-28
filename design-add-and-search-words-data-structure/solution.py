class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        parent = self.trie

        for w in word:
            if w not in parent:
                parent[w] = {}
            parent = parent[w]
        parent["word"] = word

    def search(self, word: str) -> bool:
        return self._dfsSearch(self.trie, word, 0)

    def _dfsSearch(self, parent: hash, word: str, i: int) -> str:
        if (i == len(word)):
            return ("word" in parent)
        if word[i] == ".":
            # print("word={}, i={}, word[i]={}".format(word, i, word[i]))
            for char in parent:
                if char == "word":
                    continue
                if (self._dfsSearch(parent[char], word, i + 1)):
                    return True
            return False

        if (word[i] in parent):
            return self._dfsSearch(parent[word[i]], word, i + 1)
        else:
            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
