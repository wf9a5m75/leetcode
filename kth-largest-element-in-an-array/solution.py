class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, k)

    def quickSelect(self, A, start, end, K):
        if (start >= end):
            return A[start]

        pivot_index = random.randint(start, end)
        pivot = A[pivot_index]
        i = start
        A[pivot_index], A[end] = A[end], A[pivot_index]

        for j in range(start, end):
            if (A[j] > pivot):
                A[i], A[j] = A[j], A[i]
                i += 1
        A[end], A[i] = A[i], A[end]
        if i < K - 1:
            return self.quickSelect(A, i + 1, end, K)
        elif i == K - 1:
            return A[i]
        else:
            return self.quickSelect(A, start, i - 1, K)
                    
