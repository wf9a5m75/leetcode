class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        results = []

        def walker(currIdx, path):
            # add the current index to the path
            path.append(currIdx)

            if len(graph) -1 == currIdx:
                results.append(path)
                return

            currNode = graph[currIdx]
            for toIdx in currNode:
                walker(toIdx, path.copy())

        walker(0, [])
        return results
