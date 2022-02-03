class DisJoint:
    def __init__(self, n: int):
        self.connected = list(range(n))
        self.rank = [1] * n
    def findRoot(self, x: int) -> int:
        if (self.connected[x] == x):
            return x
        self.connected[x] = self.findRoot(self.connected[x])
        return self.connected[x]

    def union(self, x: int, y: int):
        rootX = self.findRoot(x)
        rootY = self.findRoot(y)
        if (rootX != rootY):
            diff = self.rank[rootX] - self.rank[rootY]
            if diff < 0:
                self.connected[rootX] = rootY
            elif diff > 0:
                self.connected[rootY] = rootX
            else:
                self.connected[rootY] = rootX
                self.rank[rootX] += 1
    def isConnected(self, x: int, y: int)->bool:
        rootX = self.findRoot(x)
        rootY = self.findRoot(y)
        return rootX == rootY

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        disJoint = DisJoint(n)

        for v1, v2 in edges:
            disJoint.union(v1, v2)


        return disJoint.isConnected(source, destination)
