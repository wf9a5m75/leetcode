class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # To prevent duplicate results,
        # we need to sort the array first
        candidates.sort()

        N = len(candidates)

        # Using backtrack, we approach all possible cases.
        #
        def backtrack(start: int, sumSoFar: int, path: List[int]) -> List[List[int]]:
            if (sumSoFar == target):
                return [path.copy()]

            results = []
            i = start
            while(i < N) and (sumSoFar + candidates[i] <= target):
                path.append(candidates[i])
                results += backtrack(i, sumSoFar + candidates[i] , path)
                path.pop()
                i += 1

            return results


        return backtrack(0, 0, [])
