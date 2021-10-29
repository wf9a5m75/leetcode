class Solution:
    def __init__(self):
        self.mem = set()

    def numTilePossibilities(self, tiles: str) -> int:

        N = len(tiles)
        if (N == 0):
            return 0
        if (tiles in self.mem):
            return 0

        self.mem.add(tiles)
        # print(tiles)
        result = 1
        result += self.numTilePossibilities(tiles[1:])

        head = tiles[0]
        other = tiles[1:]
        for i in range(1, N):

            result += self.numTilePossibilities(other[:i] + head + other[i:])

        return result
        
