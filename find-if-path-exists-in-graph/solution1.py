class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if (start == end):
            return True

        vertixes = {}
        for i in range(n):
            vertixes[i] = []

        for edge in edges:
            vertixes[edge[0]].append(edge[1])
            vertixes[edge[1]].append(edge[0])

        queue = [start]
        while(queue):
            c = queue.pop(0)
            if len(vertixes[c]) == 0:
                continue

            while(vertixes[c]):
                nextV = vertixes[c].pop()
                if nextV == end:
                    return True
                queue.append(nextV)

        return False
