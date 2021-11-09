class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Negative marking approach: O(N) time, O(1) space
        """
        N = len(nums)
        for i in range(N):
            idx = abs(nums[i]) - 1
            if (nums[idx] > 0):
                nums[idx] = -nums[idx]

        ans = []
        for i in range(N):
            if (nums[i] > 0):
                ans.append(i + 1)
        return ans


    def findDisappearedNumbers_cycle_sort(self, nums: List[int]) -> List[int]:

        """
        Cycle sort approach: O(N^2) time, O(1) space
        """
        N = len(nums)

        i = 0
        while(i < N):
            if (nums[i] != -1) and (nums[i] != i + 1):
                tmp = nums[i]
                if (nums[i] != nums[tmp - 1]):
                    nums[i], nums[tmp - 1] = nums[tmp - 1], nums[i]
                else:
                    nums[i] = -1
                    i += 1
            else:
                i += 1
            # print(i, nums)

        ans = []
        for i in range(N):
            if (nums[i] == -1):
                ans.append(i + 1)
        return ans
