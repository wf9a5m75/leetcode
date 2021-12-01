class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        M, N = len(box), len(box[0])
        ans = [["."] * M for _ in range(N)]

        dstX = M - 1
        for y in range(M):

            # Initially, stones fall down to the ground
            lastE = N - 1

            for dstY in range(N - 1, -1, -1):
                src = box[y][dstY]

                if src == "*":
                    # If there is an obstacle,
                    # the one above cell should be empty
                    ans[dstY][dstX] = src
                    lastE = dstY - 1

                elif src == "#":
                    # If stone, fall down to the last empty cell
                    ans[lastE][dstX] = src

                    # The one above cell should be empty
                    lastE -= 1

            dstX -= 1

        return ans
