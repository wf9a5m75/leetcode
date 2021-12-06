class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # Since all chips are located at even or odd,
        # the all chips can gather at 0 or 1.

        # Then we can move the lower pile to the higher pile.
        # The cost is min(chips_of_even, chips_of_odd)

        chips_of_even = chips_of_odd = 0
        for i in position:
            if i % 2 == 0:
                chips_of_even += 1
            else:
                chips_of_odd += 1
        return min(chips_of_even, chips_of_odd)
