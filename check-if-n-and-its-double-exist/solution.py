class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mem = set()
        for num in arr:
            if num in mem:
                return True
            mem.add(num * 2)

        mem = set()
        for num in reversed(arr):
            if num in mem:
                return True
            mem.add(num * 2)
        return False
