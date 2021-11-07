class Solution:
    def singleNumber_another(self, nums: List[int]) -> List[int]:
        # 1.XOR all numers
        aXORb = 0
        for i in range(31, -1, -1):
            mask = 1 << i
            cnt = 0
            for val in nums:
                if (val & mask) > 0:
                    cnt += 1
            aXORb = (aXORb << 1) | (cnt % 2)

        isNegative = False
        if (aXORb & 2**31) > 0:
            isNegative = True
            aXORb = (~(aXORb + 1)) & 0xFFFFFFFF

        print(bin(aXORb), aXORb)

        # 2. Pick up the numbers which has the rightmost 1 set bit
        rightMost = aXORb & -aXORb
        a = 0
        for val in nums:
            if (val & rightMost) > 0:
                a = a ^ val

        # 3. Calcurate B
        if (isNegative):
            aXORb = ~aXORb - 1
        b = aXORb ^ a

        return [a, b]

    def singleNumber(self, nums: List[int]) -> List[int]:

        # 1.XOR all numers
        aXORb = 0
        for val in nums:
            aXORb = aXORb ^ val

        # 2. Pick up the numbers which has the rightmost 1 set bit
        rightMost = aXORb & -aXORb
        a = 0
        for val in nums:
            if (val & rightMost) > 0:
                a = a ^ val

        # 3. Calcurate B
        b = aXORb ^ a

        return [a, b]
