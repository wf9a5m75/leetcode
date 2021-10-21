
# Heap takes O(N Log K)
class KthLargestUsingHeap:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = []
        for val in nums:
            self.add(val)

    def add(self, val: int) -> int:
        if self.k == 1:
            if (len(self.h) == 0):
                self.h.append(val)
            else:
                self.h[0] = max(self.h[0], val)
        else:
            if (len(self.h) < self.k):
                heapq.heappush(self.h, val)
            else:
                heapq.heappushpop(self.h, val)
        # print(*self.h)
        return self.h[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
