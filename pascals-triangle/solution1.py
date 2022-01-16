class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        1: [0, 1, 0]
        2: [0, (0 + 1), (1 + 0), 0]
        3: [0, (0 + 1), (1 + 1), (1 + 0), 0]
        4: [0, (0 + 1), (1 + 2), (2 + 1), (1 + 0), 0]
        5: [0, (0 + 1), (1 + 3), (3 + 3), (3 + 1), (1 + 0), 0]
        """
        results = [[1]]
        for i in range(1, numRows):
            row = []
            prev = 0
            for j in range(i):
                row.append(prev + results[i - 1][j])
                prev = results[i - 1][j]
            row.append(prev)
            results.append(row)
        return results
