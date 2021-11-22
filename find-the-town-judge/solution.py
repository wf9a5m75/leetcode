class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = [0 for _ in range(n)]
        for trustGraph in trust:
            people[trustGraph[0] - 1] -= 1
            people[trustGraph[1] - 1] += 1

        for i in range(n):
            if people[i] == n - 1:
                return i + 1
        return -1
