class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        INF = float('inf')
        @cache
        def dp(i: int, ticketUpTo: int) -> int:
            if (i == N):
                return 0

            doNothing = INF
            if (ticketUpTo > 0) and (days[i] < ticketUpTo):
                doNothing = dp(i + 1, ticketUpTo)

            doSomething = INF
            for j, ticketLen in enumerate([1,7,30]):
                doSomething = min(doSomething, costs[j] + dp(i + 1, days[i] + ticketLen))
            return min(doSomething, doNothing)
        return dp(0, 0)
