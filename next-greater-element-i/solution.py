class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #
        # Reverse approach
        #
        stack = []
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

        # Build the answer
        result = []
        for num1 in nums1:
            result.append(mem[num1])

        return result


    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #
        # Forward approach
        #
        stack = []
        mem = {}
        for num2 in nums2:

            # The smaller numbers than num2 are appeared before.
            # It means there is no greater number the current num2.
            while(stack) and (num2 > stack[-1]):
                mem[stack.pop()] = num2

            # There is a possibility that
            # there is no value, the greater number than the current num2,
            # so we put num2 = -1
            mem[num2] = -1

            stack.append(num2)

        # Build the answer
        result = []
        for num1 in nums1:
            result.append(mem[num1])

        return result
