class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = [[] for _ in range(n + 1)]
        for v1,v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        q = [source]
        while(q):
            nextQ = []
            while(q):
                curr = q.pop()
                if (len(graph[curr]) == 0):
                    continue

                if curr == destination:
                    return True
                nextQ += graph[curr]

                graph[curr] = []
            q = nextQ
        return False
                
