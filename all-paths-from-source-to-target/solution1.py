class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        results = []

        def walker(currIdx, path):
            # add the current index to the path
            path.append(currIdx)

            # Stop traversing if we visit `n-1`
            if len(graph) -1 == currIdx:
                results.append(path.copy())
                path.pop()
                return

            # Move to the next nodes
            currNode = graph[currIdx]
            for toIdx in currNode:
                walker(toIdx, path)

            path.pop()

        # We approach with backtracking
        walker(0, [])
        return results
