from collections import Counter
import heapq
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # make a counter dictionary
        # 3:4
        # 5:3
        # 2:2
        # 7:1
        #
        # n = 10 > target = 5
        #
        counts = Counter(arr)

        distinctVals = heapq.nlargest(len(counts), counts, key=counts.get)

        n = len(arr)
        half = n >> 1
        i = 0
        while(n > half):
            n -= counts[distinctVals[i]]
            i +=1
        return i
