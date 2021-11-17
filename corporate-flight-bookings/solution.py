class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n
        for booking in bookings:
            first, last, seats = booking

            # Reserves some seats
            ans[first - 1] += seats

            # Since the last is inclusive,
            # seats number decreases at last + 1
            if (last < n):
                ans[last] -= seats

        # Sums up all seats on each time
        for i in range(n - 1):
            ans[i + 1] = ans[i] + ans[i + 1]

        return ans
