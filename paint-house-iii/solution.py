class Solution:
    def minCost_backtrack(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        INF = float("inf")
        @cache
        def dp(i: int, prevColor: int, groupSoFar: int) -> int:
            # Only valid combinations if all houses are painted grouped by "exactly" target
            if (i == m):
                return 0 if (groupSoFar == target) else INF

            # It's invalid grouping if the groupSoFar expands the limit
            if (groupSoFar > target):
                return INF

            paintCost = INF
            if houses[i] == 0:
                # The house[i] is not painted yet.
                # Trying all colors
                for color in range(1, n + 1):
                    estimate = (cost[i][color - 1] +
                                dp(i + 1, color, groupSoFar + int(prevColor != color)))

                    paintCost = min(paintCost, estimate)
            else:
                # If the house has been painted, just move ahead.
                if (houses[i] != prevColor):
                    paintCost = dp(i + 1, houses[i], groupSoFar + 1)
                else:
                    paintCost = dp(i + 1, prevColor, groupSoFar)
            return paintCost

        ans = INF
        if houses[0] == 0:
            # Trying from all colors
            for color in range(1, n + 1):
                tmp = cost[0][color - 1] + dp(1, color, 1)
                ans = min(ans, tmp)
        else:
            ans = dp(1, houses[0], 1)
        return ans if ans != INF else -1

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        INF = float("inf")
        dp = [[ [INF] * (target + 2) for _ in range(n + 1)] for __ in range(m + 1)]

        # Only valid combinations if all houses are painted grouped by "exactly" target
        for color in range(n + 1):
            dp[m][color][target] = 0

        for i in range(m - 1, 0, -1):
            for prevColor in range(n, 0, -1):
                for groupSoFar in range(1, target + 1):
                    paintCost = INF
                    if houses[i] == 0:
                        # The house[i] is not painted yet.
                        # Trying all colors
                        for color in range(1, n + 1):
                            estimate = (cost[i][color - 1] +
                                        dp[i + 1][color][groupSoFar + int(prevColor != color)])

                            paintCost = min(paintCost, estimate)
                    else:
                        # If the house has been painted, just move ahead.
                        if (houses[i] != prevColor):
                            paintCost = dp[i + 1][houses[i]][groupSoFar + 1]
                        else:
                            paintCost = dp[i + 1][prevColor][groupSoFar]
                    dp[i][prevColor][groupSoFar] = paintCost

        ans = INF
        if houses[0] == 0:
            # Trying from all colors
            for color in range(1, n + 1):
                tmp = cost[0][color - 1] + dp[1][color][1]
                ans = min(ans, tmp)
        else:
            ans = dp[1][houses[0]][1]
        return ans if ans != INF else -1
                
