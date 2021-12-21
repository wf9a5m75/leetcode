class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #
        # (1) Iteration approach
        #   Time complexity: O(N * N)
        #   Space complexity: O(N * N)
        #
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
