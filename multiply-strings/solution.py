class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if (num1 == "0" or num2 == "0"):
            return "0"

        N1 = len(num1)
        N2 = len(num2)
        N = N1 + N2
        result = [0] * (N)

        num1 = list(map(int, num1))
        num2 = list(map(int, num2))

        r = N - 1
        for d2 in reversed(num2):
            if (d2 != 0):
                carryUp = 0
                j = 0
                for d1 in reversed(num1):
                    p = (d1 * d2)  + carryUp
                    carryUp = p // 10
                    result[r - j] += (p % 10)
                    j += 1
                while(carryUp > 0):
                    result[r - j] += (carryUp % 10)
                    carryUp = carryUp // 10
                    j += 1

            r -= 1

        for j in range(N - 1, 0, -1):
            result[j - 1] += result[j] // 10
            result[j] %= 10

        i = 0
        while(i < N - 1) and (result[i] == 0):
            i += 1
        return "".join(map(str, result[i:]))
