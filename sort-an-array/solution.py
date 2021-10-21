import heapq
from typing import List
import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.heapSort(nums)
        # return self.mergeSort(nums)
        # return self.quickSort(nums)


    # ave: O(N log N)
    # worst: O(N log N)
    # best: O(N log N)
    def mergeSort(self, A):
        if (len(A) < 2):
            return A
        X = len(A) >> 1
        L = self.mergeSort(A[0:X])
        R = self.mergeSort(A[X:])

        L = L + R[::-1]
        B = []
        while(L):
            if (L[0] <= L[-1]):
                B.append(L.pop(0))
            else:
                B.append(L.pop())
        return B

    # ave: O(N log N)
    # worst: O(N log N)
    # best: O(N log K)    K denotes the number of kinds
    def heapSort(self, A):

        def max_heapify(A, x, N):
            k = x
            while(k < N):
                parent = k
                left = 2 * k + 1
                right = left + 1

                largest = parent
                if (left < N) and (A[parent] < A[left]):
                    largest = left
                if (right < N) and (A[largest] < A[right]):
                    largest = right
                if (largest == parent):
                    break
                else:
                    A[parent], A[largest] = A[largest], A[parent]
                    k = largest
                    x -= 1

        def build_max_heap(A):
            N = len(A)
            X = (N >> 1) - 1

            for k in range(X, -1, -1):
                max_heapify(A, k, N)
            return A

        def heapsort(A):
            A = build_max_heap(A)
            N = len(A)

            for i in range(N - 1, 0, -1):
                A[0], A[i] = A[i], A[0]
                max_heapify(A, 0, i)
            return A

        return heapsort(A)

    # ave: O(N log N)
    # worst: O(N ** 2)
    # best: O(N log N)
    def quickSort(self, A):
        queue = [(0, len(A) - 1)]
        while(len(queue)):
            start, end = queue.pop(0)
            if (start >= end):
                continue
            pivot = A[random.randint(start, end)]
            L = start
            R = end
            while(L <= R):
                while(L < end) and (A[L] < pivot):
                    L += 1
                while(R > start) and (A[R] > pivot):
                    R -=1
                if L > R:
                    break
                A[L], A[R] = A[R], A[L]
                L += 1
                R -= 1

            queue.append((start, L - 1))
            queue.append((L, end))
        return A
print(Solution().sortArray([5, 4, 1, 1, 3]))
