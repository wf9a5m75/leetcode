class Solution:
    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)
        if (N == 1):
            return 0

        # We build a key-values(list) dictionary
        # where the key is value of the array element,
        # and values are indicies of the elements
        positions = {}
        for i in range(N):
            if arr[i] not in positions:
                positions[arr[i]] = []
            positions[arr[i]].append(i)

        visited = [False] * N

        # BFS search
        queue = set()
        queue.add(0)
        stepCnt = 0
        lastIdx = N - 1

        while(queue):

            nextQ = set()
            for i in queue:

                # If visited, ignore this path
                if visited[i]:
                    continue
                visited[i] = True


                if i == lastIdx:
                    return stepCnt

                #
                # i - 1 or i + 1
                #
                if (i - 1 >= 0) and (visited[i - 1] == False) and (arr[i -1] != arr[i]):
                    nextQ.add(i - 1)

                if (i + 1 < N) and (visited[i + 1] == False) and (arr[i + 1] != arr[i]):
                    nextQ.add(i + 1)

                #
                # Jump to the same value indicies
                #
                if (arr[i] not in positions):
                    continue
                indiciesOfsameValues = positions[arr[i]]
                for idx in indiciesOfsameValues:
                    if (visited[idx]):
                        continue

                    nextQ.add(idx)

                del positions[arr[i]]
            stepCnt += 1

            queue = nextQ


            
