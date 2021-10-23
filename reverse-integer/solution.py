class Solution:
    def reverse(self, x: int) -> int:
        if (x >= -9) and (x <= 9):
            return x

        isNegative = False
        if (x < 0):
            isNegative = True
            x = -x
        x = str(x)
        ans = x[::-1]
        if len(ans) == 10:
            # Check the value does not exceed between 2147483647 and -2147483648
            #
            # The "margin" variable works following case:
            #   -2147483648
            #       ↓
            #    2143847412
            #
            #    2 - 2 = 0
            #    1 - 1 = 0
            #    4 - 4 = 0
            #    7 - 3 = 4
            #    4 - 8 = -4, but we have 40 (=4*10) margin. That's why this is OK
            #     ...
            margin = 0
            bounds = [2,1,4,7,4,8,3,6,4]
            for i in range(9):
                if (margin == 0) and (int(ans[i]) > bounds[i]):
                    return 0
                margin = margin * 10 + (bounds[i] - int(ans[i]))
            if ((isNegative and int(ans[9]) > 8) or
               (not isNegative and int(ans[9]) > 7)):
                return 0
        if isNegative:
            ans = "-" + ans
        ans = int(ans)
        return ans

            
