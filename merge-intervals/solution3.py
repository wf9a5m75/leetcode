class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort by start time
        intervals.sort(key = lambda x: x[0])

        results = []
        for interval in intervals:

            # If no result so far, or last time span does not contain the current interval,
            # just add the current interval
            if (len(results) == 0) or (results[-1][1] < interval[0]):
                results.append(interval)
            else:
                # Since intervals have been sorted by starting time,
                # all previous apeared intervals are started already.
                # Therefore, we just need to expand the end time
                results[-1][1] = max(results[-1][1], interval[1])
        return results
