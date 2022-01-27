class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hq = []
        self.k = k
        self.cnt = 0
        for num in nums:
            if self.cnt < k:
                heapq.heappush(self.hq, num)
                self.cnt += 1
            elif num >= self.hq[0]:
                heapq.heappushpop(self.hq, num)



    def add(self, val: int) -> int:
        if (self.cnt < self.k):
            heapq.heappush(self.hq, val)
            self.cnt += 1
        elif val >= self.hq[0]:
            heapq.heappushpop(self.hq, val)

        return self.hq[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
