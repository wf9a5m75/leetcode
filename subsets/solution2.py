class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #
        # (2) Backtracking approach
        #
        outputs = []

        # backtracking
        def backtracking(k, n, first = 0, curr = []):
            # if the combination is done
            if (len(curr) == k):
                outputs.append(curr.copy())
                return

            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])

                # use next integers to complete the combination
                backtracking(k, n, i + 1, curr)

                curr.pop()


        n = len(nums)
        for k in range(n + 1):
            backtracking(k, n)
        return outputs
