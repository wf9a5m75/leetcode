class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = deque()
        q.append((0,[0]))
        goal = len(graph) - 1

        results = []
        while(q):
            curr, path = q.popleft()
            if (curr == goal):
                results.append(path)
                continue

            for vertix in graph[curr]:
                path2 = path.copy()
                path2.append(vertix)
                q.append((vertix, path2))
        return results
