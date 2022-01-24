def stockProfit6(prices: List[int]) -> int:

    N = len(prices)
    dp = [[0] * 2 for _ in range(N + 2)]

    for i in range(N - 1, -1, -1):
        for holding in range(2):
            # 株を持っていても居なくても「何もしない」ケースは必要
            doNothing = dp[i + 1][holding]

            doSomething = 0
            if holding == 0:
                # 株を買う
                doSomething = -prices[i] + dp[i + 1][1]
            else:
                # 株を売る
                doSomething = prices[i] + dp[i + 2][0]
            # 利益が最大になるものをチョイス
            dp[i][holding] = max(doSomething, doNothing)

    return dp[0][0]
