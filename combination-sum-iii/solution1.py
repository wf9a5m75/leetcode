class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtracking(path, remain, curr):
            if len(path) == k:
                if remain == 0:
                    ans.append(path.copy())
                return
            for i in range(curr + 1, 10):
                if remain - i >= 0:
                    path.append(i)
                    backtracking(path, remain - i, i)
                    path.pop()
        backtracking([], n, 0)

        return ans
    
