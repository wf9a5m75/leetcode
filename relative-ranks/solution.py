class Solution:
    def findRelativeRanks(self, scoreList: List[int]) -> List[str]:
        scoreIdx = {}

        ranks = []
        for i, score in enumerate(scoreList):
            scoreIdx[score] = i
            heapq.heappush(ranks, score)

        n = len(scoreList)
        ranking = heapq.nlargest(n, ranks)
        scoreToRank = {}
        for i in range(n):
            if i == 0:
                scoreToRank[ranking[i]] = "Gold Medal"
            elif i == 1:
                scoreToRank[ranking[i]] = "Silver Medal"
            elif i == 2:
                scoreToRank[ranking[i]] = "Bronze Medal"
            else:
                scoreToRank[ranking[i]] = str(i + 1)

        results = []
        for score in scoreList:
            results.append(scoreToRank[score])

        return results
