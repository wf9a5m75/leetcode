class Solution:
    def getLucky(self, s: str, k: int) -> int:

        #
        # Convert: "zbax" ➝ 262124
        #
        total = 0
        for char in s:
            num = ord(char) - 96
            bias = 1
            tmp = 0
            while(num > 0):
                tmp += (num % 10) * bias
                num = num // 10
                bias *= 10
            total = total * bias + tmp

        #
        # Convert: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
        #
        num = total
        while(k > 0):
            total = 0
            bias = 1
            while(num > 0):
                total += (num % 10)
                num = num // 10

            num = total
            k -= 1

        return num
