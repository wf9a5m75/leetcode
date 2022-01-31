class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        def convertToArray(log: str) -> List[Union[int, str, int]]:
            tmp = log.split(':')
            return [int(tmp[0]), tmp[1], int(tmp[2])]

        # Converts log string to [int, string, int]
        logs = list(map(convertToArray, logs))

        stack = deque()
        functions = [0] * n
        for log in logs:
            if log[1] == "start":
                stack.append(log)
            else:

                # Calculates the exclusive time for the current function.
                startLog = stack.pop()
                execTime = log[2] - startLog[2] + 1
                functions[log[0]] += execTime

                # The next level function has been slept during the previous function was executed.
                # So, just reduces the execTime.
                if len(stack):
                    top = stack[-1]
                    functions[top[0]] -= execTime
        return functions
