class Solution:
    def findParent(self, islands: dict, idx: int) -> str:
        while(islands[idx] != idx):
            idx = islands[idx]
        return idx

    def numIslands(self, grid: List[List[str]]) -> int:
        #
        #  BFS approach
        #    Time complexity: O(M * N)
        #    Space complexity: O(M * N)
        #
        M, N = len(grid), len(grid[0])
        islands = {}
        islandIdx = 1

        dp = [[0] * (N + 1) for _ in range(M + 1)]

        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == "1":
                    indicies = []
                    upIdx = dp[y][x + 1]
                    leftIdx = dp[y + 1][x]
                    if (upIdx > 0) and (leftIdx > 0):
                        if (upIdx == leftIdx):
                            idx = upIdx
                        else:
                            # Union two regions
                            rootA = self.findParent(islands, upIdx)
                            rootB = self.findParent(islands, leftIdx)
                            islands[rootA] = islandIdx
                            islands[rootB] = islandIdx
                            islands[islandIdx] = islandIdx  # parent = itself
                            idx = islandIdx

                            islandIdx += 1
                    elif (upIdx > 0):
                        idx = upIdx
                    elif (leftIdx > 0):
                        idx = leftIdx
                    else:
                        # Found a new region
                        islands[islandIdx] = islandIdx  # parent = itself
                        idx = islandIdx
                        islandIdx += 1
                    dp[y + 1][x + 1] = idx


        #     print(*dp[y])
        # print(*dp[y + 1])
        uniqueRegions = set()
        for idx in islands:
            # find parent
            root = self.findParent(islands, idx)
            uniqueRegions.add(root)
        return len(uniqueRegions)
