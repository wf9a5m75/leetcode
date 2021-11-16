class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        N = len(arr)
        dp = [0] * (N + 1)
        for i in range(N):
            dp[i + 1] = dp[i] ^ arr[i]

        ans = []
        for query in queries:
            L, R = query
            ans.append(dp[R + 1] ^ dp[L])
        return ans
