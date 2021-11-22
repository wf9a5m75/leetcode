class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n

        queue = [0]
        while(queue):
            c = queue.pop(0)
            if visited[c]:
                continue
            visited[c] = True
            for key in rooms[c]:
                if visited[key] == False:
                    queue.append(key)
        for i in range(n):
            if (visited[i] == False):
                return False
        return True
