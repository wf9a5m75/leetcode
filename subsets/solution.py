class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #
        # (1) Iteration approach
        #

        """
        [] + [1] => [1]
        ----
        [] + [2] => [2]
        [1] + [2] => [1, 2]
        ----
        [] + [3] => [3]
        [1] + [3] => [1, 3]
        [2] + [3] => [2, 3]
        [1, 2] + [3] => [1, 2, 3]
        """
        results = [
            []
        ]
        for num in nums:

            # Generate new combination using previous result
            for i in range(len(results)):
                # print(results[i], "+", "[{}]".format(num), "=>", results[i] + [num])
                results.append(results[i] + [num])
            # print("----")
        return results

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
