class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        N = len(candidates)

        def backtrack(i: int, target: int) -> List[List[int]]:
            results = []
            for j in range(i, N):
                candidate = candidates[j]

                if (target  - candidate > 0):
                    others = backtrack(j, target - candidate)

                    for other in others:
                        other.insert(0, candidate)
                        results.append(other)

                elif (target  - candidate == 0):
                    results.append([candidate])
                else:
                    break
            return results

        return backtrack(0, target)
