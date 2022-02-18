class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        N = len(num)
        for i in range(N):

            while(stack) and (k > 0) and (num[i] < stack[-1]):
                stack.pop()
                k -= 1
            stack.append(num[i])

        while(k > 0) and (stack):
            stack.pop()
            k -= 1

        ans = "".join(stack)
        return ans.lstrip("0") or "0"
