class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(arr: List[int]) -> List[List[int]]:
            if (len(arr) == 1):
                return [arr.copy()]

            N = len(arr)
            results = []
            prev = -11
            for i in range(N):

                # If prev == arr[i],
                # we already generated the permutation.
                # Thus, skip it.
                if prev == arr[i]:
                    continue
                prev = arr[i]

                others = backtrack(arr[:i] + arr[i+1:])
                for other in others:
                    results.append([arr[i]] + other)
            return results

        # To detect duplicated numbers, we need sorting
        nums.sort()
        return backtrack(nums)
