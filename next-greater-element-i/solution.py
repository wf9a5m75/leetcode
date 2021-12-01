class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = deque()
        mem = {}
        for num2 in reversed(nums2):

            # Keep the greater numbers than the current num2
            while(stack) and (num2 > stack[-1]):
                stack.pop()

            # The top of the stack is always greater number than num2
            if stack:
                mem[num2] = stack[-1]

            # if stack is empty, no greater number after the current num2
            else:
                mem[num2] = -1

            stack.append(num2)

        result = []
        for num1 in nums1:
            result.append(mem[num1])

        return result
