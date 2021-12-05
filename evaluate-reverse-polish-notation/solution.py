class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # print(tokens)
        stack = []
        operaters = {
            "+": lambda a,b: a + b,
            "-": lambda a,b: a - b,
            "*": lambda a,b: a * b,
            "/": lambda a,b: int(a / b)  # "//" != "int(a/b)"
        }
        for token in tokens:
            if token in operaters:
                b = stack.pop()
                a = stack.pop()
                # print(a, token, b)
                stack.append(operaters[token](a, b))
            else:
                stack.append(int(token))
        return stack.pop()
