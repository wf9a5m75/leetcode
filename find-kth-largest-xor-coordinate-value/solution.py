import random
class Solution:
    def kthLargestValue(self, A: List[List[int]], k: int) -> int:
        m = len(A)
        n = len(A[0])

        h = []

        for y in range(m):
            for x in range(n):
                if y == 0:
                    if x > 0:
                        A[y][x] = A[y][x] ^ A[y][x - 1]
                else:
                    if x > 0:
                        A[y][x] = A[y][x] ^ A[y][x - 1] ^ A[y - 1][x] ^ A[y - 1][x - 1]
                    else:
                        A[y][x] = A[y][x] ^ A[y - 1][x]
                h.append(A[y][x])

        # --------------
        # quick sort is O(N log N)
        # Actually, this was the fastest.
        # --------------
        h.sort()
        return h[m * n - k]

        # --------------
        #  heapq is O(N log k),
        #  it should be better than quick sort.
        #  But it needs also k times.
        #  so O(k * N log K). That's why it's slow (I guess)
        # --------------
        # h = list(map(lambda x: -x, h))
        # rank = heapq.nsmallest(k, h)
        # return -rank[-1]

        # --------------
        #  QuickSelect is O(N), so it should be fastest.
        #  But I got the time limit exceeded
        # --------------
        # ans = self.quickSelect(h, k)
        # return ans

    def quickSelect(self, A, k):
        sizeA = len(A)
        if (sizeA < k):
            return -1

        start = 0
        end = sizeA - 1
        finalK = sizeA - k
        while(start <= end):
            pivot = random.randint(start, end)
            pIndex = self.quickSelectPatition(A, start, end, pivot)
            if (pIndex == finalK):
                return A[finalK]
            elif pIndex < finalK:
                start = pIndex + 1
            else:
                end = pIndex - 1

    def quickSelectPatition(self, A, start, end, pivot):
        A[pivot], A[end] = A[end], A[pivot]
        swapIdx = start
        for i in range(start, end):
            if (A[i] < A[end]):
                A[i], A[swapIdx] = A[swapIdx], A[i]
                swapIdx += 1
        A[end], A[swapIdx] = A[swapIdx], A[end]
        return swapIdx
