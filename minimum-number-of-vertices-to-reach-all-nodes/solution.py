class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        parents = [0] * n
        for edge in edges:
            parents[edge[1]] += 1
        ans = []
        for i in range(n):
            if parents[i] == 0:
                ans.append(i)
        return ans
