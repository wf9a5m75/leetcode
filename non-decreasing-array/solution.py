class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nums.insert(0, -10**6)
        nums.append(10**6)

        modified = False
        N = len(nums)
        dpLtoR = [0] * N
        dpRtoL = [0] * N
        i = 1
        while(0 < i < N - 1):
            if (nums[i - 1] > nums[i]):
                if (modified):
                    return False

                modified = True
                if nums[i - 1] > nums[i + 1]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                i -= 1
            else:
                i += 1
        return True
