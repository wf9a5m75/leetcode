class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        zero = ord("0")
        N = len(num)
        for i in range(N):

            d = ord(num[i]) - zero
            while(stack) and (k > 0) and (d < stack[-1]):
                stack.pop()
                k -= 1
            stack.append(d)

        while(k > 0) and (stack):
            stack.pop()
            k -= 1

        ans = []
        while(stack):
            ans.insert(0, str(stack.pop()))

        while(ans) and (ans[0] == "0"):
            ans.pop(0)
        if (len(ans) == 0):
            ans = ["0"]

        return "".join(ans)
