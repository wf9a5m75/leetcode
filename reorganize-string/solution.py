from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = list(map(lambda x: (-x[1], x[0]), list(Counter(s).items())))
        heapq.heapify(freq)

        result = [""]
        hold = None
        while(freq):
            cnt = 0
            char = ''
            if hold:
                # pop() -> push()
                cnt, char = heapq.heapreplace(freq, hold)
                hold = None
            else:
                cnt, char = heapq.heappop(freq)
            if (result[-1] != char):
                result.append(char)
                cnt += 1
                if cnt < 0:
                    hold = (cnt, char)
            else:
                hold = (cnt, char)
        if (len(result) - 1 == len(s)):
            return "".join(result)
        else:
            return ""
