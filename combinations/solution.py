class Solution:
    def __init__(self):
        self.dp = {}

    def generate(self, s: int, n: int, k: int) -> List[List[int]]:
        results = []
        key = "{}:{}:{}".format(s, n, k)
        if (key in self.dp):
            return self.dp[key]

        if (k > 1):
            for i in range(s, n + 1):
                others = self.generate(i + 1, n, k - 1)
                for other in others:
                    result = [i] + other
                    if (len(result) == k):
                        results.append(result)
                    else:
                        self.dp[key] = results
                        return results
        else:
            for i in range(s, n + 1):
                results.append([i])
        self.dp[key] = results
        return results

    def combine(self, n: int, k: int) -> List[List[int]]:

        return self.generate(1, n, k)
