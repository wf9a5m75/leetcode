class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        # Query:
        #   trips = [[2,1,5],[3,3,7]]
        #   capacity = 4
        #
        #<init>
        #  dp = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        #
        #<[2,1,5]>
        #  dp = [0, 2, 0, 0, 0, -2, 0, 0, 0]
        #
        #<[3,3,7]>
        #  dp = [0, 2, 0, 3, 0, -2, 0, -3, 0]
        #
        #-----------------
        # Then dp[i + 1] += dp[i], which denotes
        #   dp[i] : number of passengers at the i
        #   dp[i + 1] : number of pick up people
        #
        #  dp = [0, (0 + 2), 0, 3, 0, -2, 0, -3, 0]
        #        i
        #
        #  dp = [0, 2, (2 + 0), 3, 0, -2, 0, -3, 0]
        #           i
        #
        #  dp = [0, 2, 2, (2 + 3), 0, -2, 0, -3, 0]
        #              i
        #  Since 2 + 3 > 4, return False
        dp=[0] * 1002

        for trip in trips:
            numPassengers, pickUp, dropOff = trip

            dp[pickUp] += numPassengers
            dp[dropOff] -= numPassengers

        if (dp[0] > capacity):
            return False
        for i in range(1001):
            dp[i + 1] += dp[i]
            if (dp[i + 1] > capacity):
                return False
        return True
