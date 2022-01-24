def stockProfit5(prices: List[int]) -> int:

    N = len(prices)
    dp = [[[0] * 2 for _ in range(2)] for __ in range(N + 1)]

    for i in range(N - 1, -1, -1):
        for holding in range(2):
            for coolDown in range(2):
                # 株を持っていても居なくても「何もしない」ケースは必要
                doNothing = dp[i + 1][holding][0]

                doSomething = 0
                # クールダウン中でなければ何かできる
                if coolDown == 0:
                    if holding == 0:
                        # 株を買う
                        doSomething = -prices[i] + dp[i + 1][1][0]
                    else:
                        # 株を売る
                        doSomething = prices[i] + dp[i + 1][0][1]
                # 利益が最大になるものをチョイス
                dp[i][holding][coolDown] = max(doSomething, doNothing)

    return dp[0][0][0]
    
