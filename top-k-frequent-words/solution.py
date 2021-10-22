from collections import Counter
from functools import cmp_to_key

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        frequencies = Counter(words)
        def cmp_freq(a, b):
            diff = frequencies[a] - frequencies[b]
            if diff != 0:
                return diff
            for i in range(min(len(a), len(b))):
                if a[i] != b[i]:
                    # Since nlargest is the same as "sorted(iterable, key=key, reverse=True)[:n]",
                    # we need to bring the bigger one is front.
                    # That's why "ord(b[i]) - ord(a[i])"
                    return ord(b[i]) - ord(a[i])
            return (len(b) - len(a))
        ranks = heapq.nlargest(k, frequencies, key=cmp_to_key(cmp_freq))
        return ranks
