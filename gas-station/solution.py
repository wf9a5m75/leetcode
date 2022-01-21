class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        N = len(gas)

        remainGas = 0
        totalCost = 0

        # Try from start 0
        start = 0
        for i in range(N):
            remainGas += gas[i] - cost[i]

            if (remainGas < 0):
                # If remainGas is less than zero,
                # it means all start points from the start to i fail.
                #
                # Therefore, we try from i + 1
                start = i + 1
                totalCost += remainGas
                remainGas = 0

        totalCost += remainGas
        if totalCost < 0:
            return -1
        else:
            return start
