
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Since all edges connect to the center,
        # we need to check only two edges

        if edges[0][0] == edges[1][0] or edges[0][1] == edges[1][0]:
            return edges[1][0]
        elif edges[0][0] == edges[1][1] or edges[0][1] == edges[1][1]:
            return edges[1][1]
        else:
            return edges[0][1]

    def findCenter_slow(self, edges: List[List[int]]) -> int:
        N = len(edges) + 1
        visit = [0] * N
        for edge in edges:
            visit[edge[0] - 1] += 1
            visit[edge[1] - 1] += 1

        for i in range(N):
            if (visit[i] == N - 1):
                return i + 1
