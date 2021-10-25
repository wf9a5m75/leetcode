class Solution:
    def countAndSay(self, n: int) -> str:
        """
        dp[1] = 1

        Counter(dp[1])
        dp[2] =    1 -> 1   One One

        Counter(dp[2])
        1 -> 2  Two one

        Counter(dp[3])
        1 -> 1
        2 -> 1
        One two one one
        """
        prevWord = "1"

        for i in range(2, n + 1):
            prev = None
            cnt = 0
            work = []
            for d in (prevWord + "x"):
                if d != prev:
                    if cnt > 0:
                        work.append("{}{}".format(cnt, prev))
                    cnt = 1
                    prev = d
                else:
                    cnt += 1
            prevWord = "".join(work)
        return prevWord
        
