class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # To prevent duplicated results,
        # sort the array
        candidates.sort()

        N = len(candidates)
        def backtrack(start: int, sumSoFar: int, path: List[int]) -> List[List[int]]:
            if (sumSoFar == target):
                return [path.copy()]

            results = []
            i = start
            prev = -1
            while(i < N) and (sumSoFar + candidates[i] <= target):
                #
                # prevent the duplicated results
                #
                if (prev == candidates[i]):
                    i += 1
                    continue
                prev = candidates[i]

                # Since we can use each number in candidates may only be used once,
                # we start from i + 1 next time
                path.append(candidates[i])
                results += backtrack(i + 1, sumSoFar + candidates[i], path)
                path.pop()

                i += 1
            return results

        return backtrack(0, 0, [])
    
