class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start: int, sumSoFar: int, path: List[int]) -> List[List[int]]:

            # We can add a result if conditions are satisfied
            pathN = len(path)
            if (pathN == k) and (sumSoFar == n):
                return [path.copy()]

            # Try to sum up a digit number
            results = []
            i = start
            while(pathN < k) and (i < 10) and (sumSoFar + i <= n):

                # Since we can't use the same digit number,
                # we need to start from i + 1
                path.append(i)
                results += backtrack(i + 1, sumSoFar + i, path)
                path.pop()
                i += 1
            return results

        # We can sum up only number from 1 to 9.
        # So we start from 1
        return backtrack(1, 0, [])
