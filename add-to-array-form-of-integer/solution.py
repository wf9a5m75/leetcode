class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = []
        idx = len(num) - 1
        carryUp = 0
        while(k > 0) or (idx >= 0):
            kVal = k % 10
            k = int(k / 10)
            if (idx >= 0):
                n = num[idx]
                idx -= 1
            else:
                n = 0
            s = carryUp + kVal + n
            result.insert(0, s % 10)
            carryUp = int(s / 10)
        if carryUp > 0:
            result.insert(0, carryUp)
        return result
