class DisJoint:
    def __init__(self, N: int):
        self.connected = list(range(N))
        self.rank = [1] * N

    def findRoot(self, x: int) -> int:
        if (self.connected[x] == x):
            return x
        self.connected[x] = self.findRoot(self.connected[x])
        return self.connected[x]

    def union(self, x: int, y: int):
        rootX = self.findRoot(x)
        rootY = self.findRoot(y)
        if (rootX != rootY):
            if (self.rank[rootX] < self.rank[rootY]):
                self.connected[rootX] = rootY
            elif (self.rank[rootX] > self.rank[rootY]):
                self.connected[rootY] = rootX
            else:
                self.connected[rootX] = rootY
                self.rank[rootY] += 1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        disJoint = DisJoint(N)

        # Create indicies sets
        for pair in pairs:
            disJoint.union(pair[0], pair[1])

        # Pick up characters
        chars = defaultdict(list)
        for i in range(N):
            groupId = disJoint.findRoot(i)
            chars[groupId].append(s[i])

        # sort
        for groupId in chars:
            chars[groupId].sort()

        ans = []
        for i in range(N):
            groupId = disJoint.findRoot(i)
            ans.append(chars[groupId].pop(0))

        return "".join(ans)
