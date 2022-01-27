import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)
        return heapq.nlargest(k, frequencies, key=lambda x: frequencies[x])

                
