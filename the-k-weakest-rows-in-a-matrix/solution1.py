class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        hq = []
        M, N = len(mat[0]), len(mat)

        for r, row in enumerate(mat):
            soldiers = 0
            while(soldiers < M) and (row[soldiers] == 1):
                soldiers += 1

            if (r < k):
                heapq.heappush(hq, (-soldiers, -(r + 1)))
            else:
                heapq.heappushpop(hq, (-soldiers, -(r + 1)))

        results = []
        for i in range(k):
            soldiers, r = heapq.heappop(hq)
            results.insert(0, -(r + 1))
        return results
