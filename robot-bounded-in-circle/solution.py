class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # https://leetcode.com/problems/robot-bounded-in-circle/discuss/290856/JavaC%2B%2BPython-Let-Chopper-Help-Explain

        #
        # The robot is on a circle either if
        #   (1) it comes back to the origin<0,0> or
        #   (2) the last direction does not the same as the start direction
        #
        # The (2), the robot faces north, then turn right.
        # After that, turn right, then turn right.
        # The robot comes back to the original position.
        #
        # Even if the instructions include left or right,
        # it's the same result.
        #
        # The different situation occurs
        # when the robot faces north when the first instruction ends.
        #
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == 'R': dx, dy = dy, -dx
            if i == 'L': dx, dy = -dy, dx
            if i == 'G': x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0,1)

                
