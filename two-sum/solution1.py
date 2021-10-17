def binarySearch(A, target):
    left = 0
    right = len(A)
    while(left != right):
        mid = (left + right) >> 1
        if (A[mid][1] < target):
            left = mid + 1
        else:
            right = mid
    return left

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, val in enumerate(nums):
            A.append((i, val))

        A.sort(key = lambda x: x[1])

        sizeA = len(A)
        for i, val in enumerate(nums):
            rest = target - val
            pos = binarySearch(A, rest)
            if (pos < sizeA) and (A[pos][1] == rest):
                if (A[pos][0] == i) and (A[pos][1] == rest):
                    pos += 1
                if (pos < sizeA) and (A[pos][1] == rest):
                    return [min(i, A[pos][0]), max(i, A[pos][0])]
