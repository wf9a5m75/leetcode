class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        stack = []
        ans = [0] * N
        for curr_day in range(N):
            while(stack) and (temperatures[stack[-1]] < temperatures[curr_day]):
                prev_day = stack.pop()
                ans[prev_day] = curr_day - prev_day

            stack.append(curr_day)
        return ans
