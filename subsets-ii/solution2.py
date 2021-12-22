class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #
        # DFS approach
        #       Time complexity: O(N * 2**N)
        #       Space complexity: O(N * 2**N)
        #
        nums.sort()
        N = len(nums)

        results = []
        checked = set()
        def dfs(i: int, path: List[int]):
            if (i == N):
                key = str(path)
                if (key not in checked):
                    checked.add(key)
                    results.append(path)
                return

            # Choice 1: we don't pick the nums[i]
            dfs(i + 1, path.copy())

            # Choice 2: we choose the nums[i]
            path.append(nums[i])
            dfs(i + 1, path)

        dfs(0, [])
        return results
