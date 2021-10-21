import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        charList = []
        if (a):
            charList.append((-a, 'a'))
        if (b):
            charList.append((-b, 'b'))
        if (c):
            charList.append((-c, 'c'))

        s = ['', '']
        nextList = []

        mached = True
        loopCnt = 0
        while(charList) and (mached):
            heapq.heapify(charList)
            print(charList, s)

            mached = False
            while(charList) and (loopCnt < a + b + c):
                cnt, char = heapq.heappop(charList)
                loopCnt += 1
                if (char != s[-1]) or (char != s[-2]):
                    mached = True
                    s.append(char)
                    cnt += 1

                    # Try to add one more character
                    if (cnt < 0) and (char != s[-2]):
                        cnt += 1
                        s.append(char)

                    # Try to add another character
                    if (charList):
                        cnt2, char2 = heapq.heappop(charList)
                        s.append(char2)
                        cnt2 += 1
                        if (cnt2 < 0):
                            heapq.heappush(charList, (cnt2, char2))

                    if (cnt < 0):
                        heapq.heappush(charList, (cnt, char))


                else:
                    nextList.append((cnt, char))
            charList += nextList


        return "".join(s)
# print(Solution().longestDiverseString(7, 1, 0))
