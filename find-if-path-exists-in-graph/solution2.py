class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for v1, v2 in edges:
            if v1 not in graph:
                graph[v1] = set()
            graph[v1].add(v2)

            if v2 not in graph:
                graph[v2] = set()
            graph[v2].add(v1)


        visited = set()
        def dfs(curr: int) -> bool:
            if curr == destination:
                return True
            if (curr not in graph):
                return False

            visited.add(curr)

            for nextDst in graph[curr]:
                if (nextDst not in visited) and dfs(nextDst):
                    return True

        return dfs(source)
