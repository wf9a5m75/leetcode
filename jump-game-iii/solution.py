class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        N = len(arr)
        visited = [False] * N

        queue = [start]
        while(queue):
            curr = queue.pop(0)

            # If we already visited to i,
            # move on to the next task
            if visited[curr]:
                continue
            visited[curr] = True

            # Finish traversing if we found arr[i] == 0
            if arr[curr] == 0:
                return True

            # If we can move to the new position,
            # add it as a new task
            nextI = curr - arr[curr]
            if nextI >= 0:
                queue.append(nextI)

            nextI = curr + arr[curr]
            if nextI < N:
                queue.append(nextI)
        return False
