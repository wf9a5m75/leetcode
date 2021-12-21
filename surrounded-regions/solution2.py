class Solution:
    #
    # Union-Find approach :
    #   Time complexity: O(M * N)
    #   Space complexity: O(M * N)
    #
    def findParent(self, groups: dict, idx: str) -> str:
        if idx not in groups:
            return 0
        while(groups[idx] != idx):
            idx = groups[idx]
        return idx

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        dp = [[0] * (N + 1) for _ in range(M + 1)]

        parentIdx = 1
        groups = {}
        groupChildren = {}
        onBoarderGroups = set()

        for y in range(M):
            for x in range(N):
                thisGroup = 0
                if (board[y][x] == "O"):
                    isOnBoarder = (y == 0) or (y == M - 1) or (x == 0) or (x == N - 1)

                    upGroup = self.findParent(groups, dp[y][x + 1])
                    leftGroup = self.findParent(groups, dp[y + 1][x])

                    if (upGroup > 0) or (leftGroup > 0):

                        # If both group numbers are the same, inherits it.
                        if (upGroup == leftGroup):
                            thisGroup = upGroup

                        # Otherwise, unions to the bigger group number
                        else:
                            thisGroup = max(upGroup, leftGroup)
                            if (upGroup > 0):
                                groups[upGroup] = thisGroup
                            if (leftGroup > 0):
                                groups[leftGroup] = thisGroup
                    else:
                        # Issues a new group id
                        groups[parentIdx] = parentIdx
                        groupChildren[parentIdx] = []
                        thisGroup = parentIdx

                        parentIdx += 1

                    dp[y + 1][x + 1] = thisGroup

                    # Records the location
                    groupChildren[thisGroup].append((y, x))

                    # Marks as onBoard
                    if isOnBoarder:
                        onBoarderGroups.add(thisGroup)

        # for y in range(M + 1):
        #     print(*dp[y])

        for gIdx in list(onBoarderGroups):
            root = self.findParent(groups, gIdx)
            onBoarderGroups.add(root)

        for gIdx in groups:
            root = self.findParent(groups, gIdx)
            if root not in onBoarderGroups:
                for y, x in groupChildren[gIdx]:
                    board[y][x] = "X"
