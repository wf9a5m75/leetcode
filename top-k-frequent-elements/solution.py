from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # O(N)
        counts = Counter(nums)

        # heap sort
        # O(N log k) times
        return heapq.nlargest(k, counts.keys(), key=counts.get)


    def topKFrequent_normal(self, nums: List[int], k: int) -> List[int]:
        results = Counter(nums).most_common(k)
        results = list(map(lambda x: x[0], results))
        return results
