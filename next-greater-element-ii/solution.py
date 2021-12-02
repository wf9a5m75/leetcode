class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        stack = []
        ans = [0] * N
        for i in range(2 * N - 1, -1, -1):
            while(stack) and (nums[stack[-1]] <= nums[i % N]):
                stack.pop()
            if stack:
                ans[i % N] = nums[stack[-1]]
            else:
                ans[i % N] = -1
            stack.append(i % N)
        return ans

    def nextGreaterElements(self, nums):
        # Loop once, we can get the Next Greater Number of a normal array.
        # Loop twice, we can get the Next Greater Number of a circular array
        N = len(nums)
        stack, res = [], [-1] * N

        for j in range(2):
            for i in range(N):
                while stack and (nums[stack[-1]] < nums[i]):
                    res[stack.pop()] = nums[i]
                stack.append(i)

        return res
