class TrieNode:
    def __init__(self):
        self.dict = {}
        self.eow = False

    def __repr__(self):
        return "(eow: {}, dict: {}".format(self.eow, self.dict)

class TrieTree:
    def __init__(self):
        self.tree = TrieNode()

    def look(self):
        print(self.tree)

    def insert(self, word: str) -> None:
        root = self.tree

        for w in word:
            if (w not in root.dict):
                root.dict[w] = TrieNode()
            root = root.dict[w]
        root.eow = True

    def prefixMatch(self, word) -> str:
        root = self.tree
        path = []
        for w in word:
            if (w not in root.dict):
                return word

            root = root.dict[w]

            path.append(w)
            if (root.eow):
                return "".join(path)

        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        self.tree = TrieTree()

        # self.tree.insert("catt")
        # self.tree.insert("cat")
        # self.tree.look()
        # print("ans", self.tree.prefixMatch("catt"))
        for word in dictionary:
            self.tree.insert(word)

        results = []
        for word in (sentence.split()):
            results.append(self.tree.prefixMatch(word))

        return " ".join(results)
