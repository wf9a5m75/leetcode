class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        misMatched = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                misMatched += 1
        return misMatched
