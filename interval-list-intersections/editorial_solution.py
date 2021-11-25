class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        nA, nB = len(A), len(B)
        i = j = 0
        while(i < nA) and (j < nB):
            if (A[i][0] <= B[j][1]) and (B[j][0] <= A[i][1]):
                ans.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return ans
