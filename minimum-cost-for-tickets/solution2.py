class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        INF = float('inf')
        dp = [INF] * (N + 1)
        dp[0] = 0

        for i in range(N):
            for j, ticketLen in enumerate([1,7,30]):
                k = i
                while(k < N) and (days[k] < days[i] + ticketLen):
                    dp[k + 1] = min(dp[k + 1], dp[i] + costs[j])
                    k+=1
        return dp[N]
