class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Negative marking approach: O(N) time, O(1) space
        """
        N = len(nums)
        duplicates = []
        for i in range(N):
            idx = abs(nums[i]) - 1
            if (nums[idx] > 0):
                nums[idx] = -nums[idx]
            else:
                duplicates.append(abs(nums[i]))

        return duplicates


    def findDuplicates_slow(self, nums: List[int]) -> List[int]:
        """
        Cycle sort approach: O(N^2) time, O(1) space
        """
        N = len(nums)
        duplicates = []
        i = 0
        while(i < N):
            # print(i, nums)
            idx = nums[i] - 1
            if (nums[i] == -1) or (i + 1 == nums[idx]):
                i += 1
                continue

            if (nums[i] == nums[idx]):
                duplicates.append(nums[i])
                nums[i] = -1
                i += 1
            else:
                nums[idx],nums[i] = nums[i], nums[idx]
        return duplicates
        
