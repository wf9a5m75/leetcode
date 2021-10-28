class TrieNode:
    def __init__(self):
        self.dict = {}
        self.endOfWords = False

class Trie:

    def __init__(self):
        self.tree = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.tree
        for w in word:
            if (w not in curr.dict):
                curr.dict[w] = TrieNode()
            curr = curr.dict[w]
        curr.endOfWords = True

    def search(self, word: str) -> bool:
        curr = self.tree
        for w in word:
            if (w not in curr.dict):
                return False
            curr = curr.dict[w]
        return curr.endOfWords

    def startsWith(self, prefix: str) -> bool:
        curr = self.tree
        for w in prefix:
            if (w not in curr.dict):
                return False
            curr = curr.dict[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
