class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = [-1] * (n + 1)
        scores = [0] * (n + 1)

        for peopleA, peopleB in trust:

            # Find the root
            path = []
            while(graph[peopleB] == peopleB):
                path.append(peopleB)
                peopleB = graph[peopleB]

            graph[peopleA] = peopleB

            # Update the nodes on the path
            for p in path:
                graph[p] = peopleB

            # Increasing the score
            scores[peopleB] += 1

        # Find the town judge
        #   The town judge does not trust nobody (graph = -1)
        #   and everyone trust the judge (score = n - 1)
        for i in range(1, n + 1):
            if (graph[i] == -1) and (scores[i] == n - 1):
                return i
        return -1
