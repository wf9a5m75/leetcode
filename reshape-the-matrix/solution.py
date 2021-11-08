class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        if ((M * N) != (r * c)):
            return mat

        work = []
        for row in mat:
            work += row

        ans = []
        i = 0
        for _ in range(r):
            ans.append(work[i:i+c])
            i += c
        return ans
            
