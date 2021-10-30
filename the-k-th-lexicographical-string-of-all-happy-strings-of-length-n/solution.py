class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Converts each row to the number of soldiers
        rows = list(map(lambda row: len(list(filter(lambda x: x == 1, row))), mat))

        # Heap sort (sort by number of soldiers)
        h = []
        for i, numberOfSoldiers in enumerate(rows):
            heapq.heappush(h, (numberOfSoldiers, i))

        nthWeakest = heapq.nsmallest(k, h)

        # Makes the result
        results = []
        for weakRows in nthWeakest:
            results.append(weakRows[1])

        return results
