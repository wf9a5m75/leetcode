class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """
         n = 5 => 101b

         number of bits = int(math.log2(n)) = 2
         mask = (1 << (2 + 1)) - 1 = 111

         101b xor 111b = 010b
        """
        if (n == 0):
            return 1
        tmp = (1 << (int(math.log2(n)) + 1)) - 1
        return n ^ tmp
