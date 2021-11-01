class TrieNode:
    def __init__(self):
        self.dict = {}
        self.endOfWord = False
        self.products = []

class ProductName:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        tree = TrieNode()

        productList = []

        # Create a trie tree
        for product in products:
            holder = ProductName(product)

            root = tree
            for w in product:
                root.products.append(holder)

                if w not in root.dict:
                    root.dict[w] = TrieNode()
                root = root.dict[w]
            root.endOfWord = True
            root.products.append(holder)

        # search at most three words prefix matched with the searchWord
        results = []
        root = tree
        empty = TrieNode()
        for s in searchWord:
            if s in root.dict:
                root = root.dict[s]
            else:
                root = empty

            suggests = sorted(root.products, key = lambda x: str(x))
            if len(suggests) > 2:
                suggests = suggests[:3]
            suggests = list(map(str, suggests))
            results.append(suggests)

        return results
            
