class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        idxA = idxB = 0
        N1, N2 = len(firstList), len(secondList)
        results = []
        lastA = lastB = -1
        mem = set()

        while (idxA < N1) and (idxB < N2):
            A = firstList[idxA]
            B = secondList[idxB]

            if lastA == B[0]:
                key = "{}:{}".format(B[0], B[0])
                if key not in mem:
                    results.append([B[0], B[0]])
                    mem.add(key)

            if lastB == A[0]:
                key = "{}:{}".format(A[0], A[0])
                if key not in mem:
                    results.append([A[0], A[0]])
                    mem.add(key)

            lastA, lastB = A[1], B[1]

            # A ∋ B
            if A[0] <= B[0] <= B[1] <= A[1]:
                results.append(B)
                idxB += 1
                continue

            # A ∈ B
            if B[0] <= A[0] <= A[1] <= B[1]:
                results.append(A)
                idxA += 1
                continue

            if A[1] == B[0]:
                key = "{}:{}".format(A[1], A[1])
                if key not in mem:
                    results.append([A[1], A[1]])
                    mem.add(key)
                idxA += 1
                continue

            if B[1] == A[0]:
                key = "{}:{}".format(B[1], B[1])
                if key not in mem:
                    results.append([B[1], B[1]])
                    mem.add(key)
                idxB += 1
                continue

            if A[0] <= B[0] <= A[1] <= B[1]:
                results.append([B[0], A[1]])
                idxA += 1
                continue

            if B[0] <= A[0] <= B[1] <= A[1]:
                results.append([A[0], B[1]])
                idxB += 1
                continue

            # A and B do not overlap each other
            if A[1] < B[0]:
                idxA += 1
            else:
                idxB += 1

        return results
