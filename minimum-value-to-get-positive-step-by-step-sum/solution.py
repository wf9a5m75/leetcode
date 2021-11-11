class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        """
        Since we have to choose the startValue
        to make all sum step by step,
        we choose the value greater than the lowest value + 1.

                  sum  | bottom
        -------------------------
        (init) |   0   |    0
          -3   |  -3   |   -3
           2   |  -1   |   -3
          -3   |  -4   |   -4
           4   |   0   |   -4
           2   |   2   |   -4
         ------------------------

         -(-4) + 1 => 5


                  sum  | bottom
        -------------------------
        (init) |   0   |    0
           1   |   1   |    0
           2   |   3   |    0
         ------------------------
         -(0) + 1 => 1
        """
        s = 0
        bottom = 0
        for num in nums:
            s += num
            bottom = min(s, bottom)
        return -bottom + 1
