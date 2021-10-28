class MagicNode:
    def __init__(self):
        self.dict = {}

        # "eow" represents "end of words"
        self.eow = False

    def __repr__(self):
        return "(eow:{}, dict: {})".format(self.eow, self.dict)

class MagicDictionary:

    def __init__(self):
        self.tree = MagicNode()

    def _insertWord(self, word):
        curr = self.tree
        for w in word:
            if (w not in curr.dict):
                curr.dict[w] = MagicNode()
            curr = curr.dict[w]
        curr.eow = True

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self._insertWord(word)
        # print(self.tree)

    def _search(self, searchWord: str, root: MagicNode) -> bool:
        # print("--->", searchWord)
        curr = root
        for i, w in enumerate(searchWord):
            if (w.isupper()):
                keys = list(curr.dict.keys())
                newWord = searchWord[i+1:]
                w = w.lower()
                for char in keys:
                    if char == w:
                        continue

                    # print("  try ", char, newWord)
                    if (self._search(newWord, curr.dict[char])):
                        return True
                w = w.upper()
            if (w not in curr.dict):
                return False
            curr = curr.dict[w]
        # print("   sucess", searchWord)
        return curr.eow

    def search(self, searchWord: str) -> bool:
        # print("===")
        # print("  query: ", searchWord)

        searchWord = list(searchWord)
        for i in range(len(searchWord)):
            searchWord[i] = searchWord[i].upper()
            if (self._search("".join(searchWord), self.tree)):
                return True
            searchWord[i] = searchWord[i].lower()

        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
