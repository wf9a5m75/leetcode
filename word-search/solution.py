class Node:
    def __init__(self, val: str):
        self.val = val
        self.nexts = defaultdict(set)
        self.visited = False
        self.x = 0
        self.y = 0

    def connect(self, other):
        self.nexts[other.val].add(other)

    def __repr__(self)->str:
        return "{}({},{})".format(self.val, self.y, self.x)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        M, N = len(board), len(board[0])
        wordSet = set(word)

        dp = [[None] * N for _ in range(M)]
        directions = [(-1,0), (1,0),(0, -1), (0, 1)]
        positions = defaultdict(list)


        for y in range(M):
            for x in range(N):
                if (board[y][x] in wordSet):
                    w = board[y][x]
                    node = Node(w)
                    node.y = y
                    node.x = x
                    dp[y][x] = node
                    positions[w].append(node)

                    for direction in directions:
                        dy, dx = y + direction[0], x + direction[1]
                        if (0 <= dy < M) and (0 <= dx < N) and (dp[dy][dx] is not None):

                            dp[dy][dx].connect(node)
                            node.connect(dp[dy][dx])

        wordN = len(word)
        def dfs(i: int, curr: Node) -> bool:
            curr.visited = True

            if i + 1 == wordN:
                return True

            nextW = word[i + 1]
            for node in curr.nexts[nextW]:
                if node.visited == False:
                    if dfs(i + 1, node):
                        return True

            curr.visited = False
            return False

        for node in positions[word[0]]:
            if dfs(0, node):
                return True

        return False
