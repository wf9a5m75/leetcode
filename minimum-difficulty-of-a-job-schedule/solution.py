class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)

        # Since we have to do at least one job every day,
        # number of jobs are not enough than d days,
        # we can't do that.
        if N < d:
            return -1

        hardestRemaining = [0] * N
        hardestRemaining[N - 1] = jobDifficulty[N - 1]
        for i in range(N - 2, -1, -1):
            hardestRemaining[i] = max(hardestRemaining[i + 1], jobDifficulty[i])

        @lru_cache(2000)
        def backtrack(i: int, currentDay: int) -> int:
            # print("currentDay = {}, i = {}".format(currentDay, i))

            # The job difficulty of the last day
            if currentDay == d:
                return hardestRemaining[i]

            upTo = N - (d - currentDay)
            ans = 2 ** 31 -1
            hardestToday = 0
            for j in range(i, upTo):
                hardestToday = max(hardestToday, jobDifficulty[j])
                ans = min(ans, hardestToday + backtrack(j + 1, currentDay + 1))
            return ans

        return backtrack(0, 1)
