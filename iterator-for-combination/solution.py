class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        characters = list(characters)
        N = len(characters)

        def generate(characters, remainDepth):
            if remainDepth == 0:
                results = []
                for i in range(len(characters)):
                    results.append(characters[i])
                return results

            results = []
            for i in range(len(characters)):
                head = characters.pop(0)
                others = generate(characters.copy(), remainDepth - 1)
                results += list(map(lambda other: head + other, others))
            return results


        self.combinations = generate(characters, combinationLength - 1)

        # print(self.combinations)

    def next(self) -> str:
        return self.combinations.pop(0)

    def hasNext(self) -> bool:
        return len(self.combinations) > 0



# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
