class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Keeps smaller numbers
        stack = []
        for digit in num:

            # Throws away greater or equal numbers than digit
            while(k > 0) and (stack) and (stack[-1] > digit):
                stack.pop()

                # Reduces the deletable character counter
                k -= 1

            stack.append(digit)

        # If k > 0, we have to remove the remained k digits.
        while(k > 0) and (stack):
            stack.pop()
            k -= 1

        # Even if we still have k, it means "0"
        if k > 0:
            return "0"

        # Remove leeding "0"
        return ("".join(stack)).lstrip("0") or "0"
