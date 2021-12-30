class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # We need to find the N such that
        #   1) it contains only "1", and
        #   2) it must be "N % K = 0"

        # Since the condition #2, "N % K = 0",
        # N takes from 0 to K - 1.

        N = 1
        lengthN = 1

        # Because of N loops from 0 to K - 1,
        # if the N does not exist, the N causes a collition.
        # We check this using bit flags
        seen = 0
        while(N % k != 0):
            N = (N * 10 + 1) % k
            lengthN += 1

            mask = 1 << N

            # This N % k was checked before.
            if (seen & mask) > 0:
                return -1

            # Mark as we checked
            else:
                seen |= mask
        return lengthN
