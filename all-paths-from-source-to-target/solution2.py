class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #
        #  BFS approach
        #    Time complexity: O(2**v * V)
        #    Space complexity: O(V)
        #
        N = len(graph)
        results = []
        queue = [[0]]
        while(queue):
            curr = queue.pop(0)
            if (curr[-1] == N - 1):
                results.append(curr)
                continue

            nextQ = []
            for idx in graph[curr[-1]]:
                nextPath = curr.copy()
                nextPath.append(idx)
                queue.append(nextPath)
        return results
