class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        N = len(image[0])
        for row in image:
            L, R = 0, N - 1
            while(L <= R):
                if (L != R):
                    row[L], row[R] = 1 ^ row[R], 1 ^ row[L]
                else:
                    row[L] = 1 ^ row[L]
                L += 1
                R -= 1
        return image
