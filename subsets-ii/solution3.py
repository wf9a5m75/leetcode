class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #
        # DP approach
        #       Time complexity: O(N * 2**N)
        #       Space complexity: O(N * 2**N)
        #
        nums.sort()
        currS = [[]]

        for num in nums:
            nextS = []
            checked = set()
            for state in currS:

                # Choice 1. we don't choose the num
                key = str(state)
                if (key not in checked):
                    checked.add(key)
                    nextS.append(state.copy())

                # Choice 2. we choose the num
                state.append(num)
                key = str(state)
                if (key not in checked):
                    checked.add(key)
                    nextS.append(state)
            currS = nextS
        return currS
