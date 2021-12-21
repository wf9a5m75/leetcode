class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #
        # Backtrack approach
        #
        N = len(nums)
        def backtrack(start: int, path: List[int]) -> List[List[int]]:
            # print(start, path)
            if (start == N):
                return [path.copy()]

            path.append(nums[start])
            results = []
            for i in range(start + 1, N + 1):
                results += backtrack(i, path)
            path.pop()
            return results

        results = [[]]
        for i in range(0, N):
            results += backtrack(i, [])
        return results
