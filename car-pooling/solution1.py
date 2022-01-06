class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dp = defaultdict(int)

        for passengers, start,end in trips:
            dp[start] += passengers
            dp[end] -= passengers

        current = 0
        for eventTime in sorted(dp):
            current += dp[eventTime]
            if (current > capacity):
                return False
        return True
