class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        N = len(arr)
        minDiff = arr[N-1] - arr[0]

        results = []
        for i in range(N - 1):
            diff = arr[i + 1] - arr[i]
            if minDiff > diff:
                results.clear()
                results.append([arr[i], arr[i + 1]])
                minDiff = diff
            elif diff == minDiff:
                results.append([arr[i], arr[i + 1]])

        return results
