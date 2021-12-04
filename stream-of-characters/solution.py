class Node:
    def __init__(self):
        self.eow = False
        self.children = {}

    # def __repr__(self):
    #     return "(eow:{},child:{})".format(self.eow, self.children)

class StreamChecker:

    def __init__(self, words: List[str]):
        # Trie dictionary
        self.dic = Node()

        # Denotes the maximum length of the words
        self.maxLen = 0

        # Stream buffer for suffix searching
        self.buffer = []

        # Keeps the current buffer length usage
        self.currLen = 0

        for word in words:
            # maxLen = words[i].length <= 2000
            self.maxLen = max(self.maxLen, len(word))

            parent = self.dic
            for w in reversed(word):
                if (w not in parent.children):
                    parent.children[w] = Node()
                parent = parent.children[w]
            parent.eow = True
        # print(self.dic)

    def query(self, letter: str) -> bool:
        # If buffer + letter becomes over than
        # the maximum length of the words,
        # pop the first letter (FIFO)
        if (self.currLen + 1 > self.maxLen):
            self.buffer.pop()

        self.buffer.insert(0, letter)
        self.currLen = len(self.buffer)

        # Search the word
        parent = self.dic
        for c in self.buffer:
            if c in parent.children:
                if parent.children[c].eow:
                    return True
                parent = parent.children[c]
            else:
                # print(self.buffer)
                return False

        # We should not reach to here, but just in case
        return parent.eow



# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
