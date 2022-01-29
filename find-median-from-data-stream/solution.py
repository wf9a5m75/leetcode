class MedianFinder:
    #
    # https://leetcode.com/problems/find-median-from-data-stream/discuss/74047/JavaPython-two-heap-solution-O(log-n)-add-O(1)-find
    #

    def __init__(self):
        self.minHq = []
        self.maxHq = []

    def addNum(self, num: int) -> None:
        if (len(self.minHq) == len(self.maxHq)):
            # Move the largest value in the maximum heapq into the minumum heapq
            heapq.heappush(self.minHq, -heapq.heappushpop(self.maxHq, -num))
        else:
            # Move the smallest value in the minimum heapq into the maximum heapq
            heapq.heappush(self.maxHq, -heapq.heappushpop(self.minHq, num))


    def findMedian(self) -> float:
        if (len(self.minHq) == len(self.maxHq)):
            return (self.minHq[0] + -self.maxHq[0]) / 2
        else:
            return self.minHq[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
