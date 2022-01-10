class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        #
        # O(N) time, O(1) space
        # https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/discuss/1679483/python-or-98.72-faster-O(n)-time-O(1)-space
        #
        pCnt = nCnt = lastPcnt = firstPcnt = 0
        ans = 0
        nums.append(0)
        for num in nums:
            if num == 0:
                if (nCnt % 2 == 0):
                    ans = max(ans, pCnt + nCnt)
                else:
                    # print("pCnt = {}, nCnt = {}, firstPcnt = {}, lastPcnt = {}".format(pCnt, nCnt, firstPcnt, lastPcnt))
                    ans = max(ans, pCnt - min(firstPcnt, lastPcnt) + nCnt - 1)
                firstPcnt = lastPcnt = pCnt = nCnt = 0
            elif num < 0:
                nCnt += 1
                lastPcnt = 0
            else:
                if nCnt == 0:
                    firstPcnt += 1
                pCnt += 1
                lastPcnt += 1
        return ans
