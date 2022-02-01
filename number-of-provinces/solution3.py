class Disjoint:
    def __init__(self, N: int):
        # All cities are connected by themselves, initially.
        self.connected = list(range(N))

        # All cities tree heights are 1.
        self.rank = [1] * N

    def findRoot(self, x: int) -> int:
        if (x == self.connected[x]):
            return x
        # path compression
        self.connected[x] = self.findRoot(self.connected[x])
        return self.connected[x]

    def union(self, x: int, y: int):
        rootX = self.findRoot(x)
        rootY = self.findRoot(y)
        if (rootX != rootY):
            # Connect the shorter tree to the longer tree root.
            #
            #  1-2-3   4-5-6-7-8
            #   ↓
            #
            #  4-5-6-7-8
            #   │
            #   └1-2-3
            #
            if (self.rank[rootX] < self.rank[rootY]):
                self.connected[rootX] = rootY

            elif (self.rank[rootX] > self.rank[rootY]):
                self.connected[rootY] = rootX

            else:
                self.connected[rootX] = rootY
                self.rank[rootY] += 1

    def isConnected(self, x: int, y: int) -> bool:
        rootX = self.findRoot(x)
        rootY = self.findRoot(y)
        return rootX == rootY
    def debug(self):
        print(self.connected)
        print(self.rank)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        disjoint = Disjoint(N)

        for y in range(N):
            for x in range(N):
                if isConnected[y][x] == 1:
                    disjoint.union(y, x)


        provinces = set()
        for i in range(N):
            provinces.add(disjoint.findRoot(i))
        return len(provinces)
