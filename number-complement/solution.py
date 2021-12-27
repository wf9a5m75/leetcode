class Solution:
    def findComplement(self, num: int) -> int:
        # Get the most right bit
        #                             (n = 6) ===> 0110
        #  (1 << int(math.log2(num)) + 1) - 1 ===> 0111
        mask = (1 << (int(math.log2(num)) + 1)) - 1
        # print("{:4b}".format(mask))

        # Reverse 0 -> 1, 1 -> 0
        #
        # (n = 6) => 0110
        #     ~ 6 => 1001
        num = num ^ (2**31 - 1)
        # print("{:4b}".format(num))

        # num & mask
        #   1001 & 0100 = 0001
        # print("{:4b}".format(num & mask))
        return num & mask
