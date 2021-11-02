class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        for step in path:
            if (step == "" or step == "."):
                continue
            if (step == ".."):
                if (stack):
                    stack.pop()
                continue
            stack.append(step)
        if (len(stack) == 0):
            return "/"
        return "/" + ("/".join(stack))
