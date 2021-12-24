class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        results = []

        def backtracking(path, remain, curr):
            if (remain == 0):
                return results.append(list(path))

            for next_curr in range(curr, N):
                if ((next_curr > curr) and
                   (candidates[next_curr] == candidates[next_curr - 1])):

                    continue
                pick = candidates[next_curr]

                if (remain - pick < 0):
                    break

                path.append(pick)
                backtracking(path, remain - pick, next_curr + 1)
                path.pop()

        candidates.sort()
        path = []
        backtracking(path, target, 0)
        return results
