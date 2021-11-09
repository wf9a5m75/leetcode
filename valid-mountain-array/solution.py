class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if (len(arr) < 3) or (arr[0] > arr[1]) or (arr[-2] < arr[-1]):
            return False

        prev = -1
        hasPeak = False
        for num in arr:
            if (num == prev) or (hasPeak and prev < num):
                return False
            if (not hasPeak) and (prev > num):
                hasPeak = True
            prev = num
        return True
