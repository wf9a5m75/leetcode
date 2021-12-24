class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #
        # Monotonic stack approach
        #  Time complexity: O(N log N)
        #    Since we sort the intervals at once,
        #    we need to spend O(N log N).
        #
        #  Space complexity: O(N)
        #    The results variable takes O(N) maximumly

        # Sort by end time
        intervals.sort(key = lambda x: x[1])

        results = []
        for timeSpan in intervals:

            # If the last of results can merge to the current timeSpan,
            # we can merge it.
            while(results) and (results[-1][1] >= timeSpan[0]):
                lastTimespan = results.pop()
                timeSpan[0] = min(lastTimespan[0], timeSpan[0])
                timeSpan[1] = max(lastTimespan[1], timeSpan[1])

            # Add to the results
            results.append(timeSpan)

        return results
