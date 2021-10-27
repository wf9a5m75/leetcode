class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[1])

        results = [intervals[0]]
        for interval in intervals:
            curr = interval
            while(len(results) > 0):
                last = results.pop()
                if ((last[0] <= curr[0] <= last[1]) or
                    (last[0] <= curr[1] <= last[1]) or
                    (curr[0] <= last[0] <= curr[1]) or
                    (curr[0] <= last[1] <= curr[1])):

                    curr = [ min(last[0], curr[0]), max(last[1], curr[1]) ]
                else:
                    results.append(last)
                    break
            results.append(curr)

        return results
