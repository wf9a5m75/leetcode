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
    
    def combinationSum3_slow(self, k: int, n: int, path: List[int] = [], mem = set()) -> List[List[int]]:
        if k >= 10:
            return []

        if (k == 0):
            if (n == 0):
                key = ":".join(sorted(path))
                if key not in mem:
                    mem.add(key)
                    # print(n, path)
                    return [path.copy()]
                else:
                    return []
            else:
                return []

        results = []
        for d in range(1, 10):
            if (n - d >= 0) and (str(d) not in path):
                path.append(str(d))
                results += self.combinationSum3(k - 1, n - d, path, mem)
                path.pop()
        return results
