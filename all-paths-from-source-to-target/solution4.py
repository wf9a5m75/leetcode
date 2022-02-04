class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)

        results = []
        q = [ [0] ]
        while(q):
            nextQ = []
            while(q):
                currPath = q.pop()
                currPos = currPath[-1]
                if (currPos == n - 1):
                    results.append(currPath)
                else:
                    for nextDst in graph[currPos]:
                        nextQ.append(currPath + [nextDst])
            q = nextQ
        return results
