class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        results = []
        p1 = p2 = 0
        N1, N2 = len(firstList), len(secondList)
        while(p1 < N1) and (p2 < N2):
            # If time1.endTime does not overlap with time2.startTime:
            #   move the next time span on the firstList
            if firstList[p1][1] < secondList[p2][0]:
                p1 += 1
                continue

            # If time2.endTime does not overlap with time1.startTime:
            #   move the next time span on the firstList
            if secondList[p2][1] < firstList[p1][0]:
                p2 += 1
                continue

            # Both time spans should be overlapped each other.
            results.append([
                    max(firstList[p1][0], secondList[p2][0]),
                    min(firstList[p1][1], secondList[p2][1])
            ])

            # If time1.end is smaller than time2.end,
            # it means time1 has been finished during the time2.
            # So move on to the next time span on the firstList.
            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return results
