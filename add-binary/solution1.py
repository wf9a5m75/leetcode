class Solution:
    def addBinary(self, a: str, b: str) -> str:
        idxA, idxB = len(a) - 1, len(b) - 1
        result = deque()
        carryUp = 0
        while(idxA >= 0) and (idxB >= 0):
            aVal, bVal = int(a[idxA]), int(b[idxB])
            s = carryUp + aVal + bVal
            result.insert(0, str(s % 2))

            carryUp = s >> 1
            idxA -= 1
            idxB -= 1

        while(idxA >= 0):
            aVal = int(a[idxA])
            s = carryUp + aVal
            result.insert(0, str(s % 2))
            carryUp = s >> 1
            idxA -= 1

        while(idxB >= 0):
            bVal = int(b[idxB])
            s = carryUp + bVal
            result.insert(0, str(s % 2))
            carryUp = s >> 1
            idxB -= 1
        if carryUp != 0:
            result.insert(0, "1")

        return "".join(result)
            
