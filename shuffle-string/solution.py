class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        #
        # Simple code
        #   O(N) time complexity
        #   O(N) space complexity
        #
        N = len(indices)
        tmp = [""] * N
        for i in range(N):
            idx = indices[i]
            tmp[idx] = s[i]
        return "".join(tmp)

    def restoreString(self, s: str, indices: List[int]) -> str:

        #
        # Cycle sort
        #   O(N * N) time complexity
        #   O(1) space complexity
        #
        N = len(s)
        s = list(s)
        for i in range(N):
            while(i != indices[i]):
                j = indices[i]
                s[ j ], s[i] = s[i], s[ j ]
                indices[i], indices[j] = indices[j], indices[i]
        return "".join(s)
