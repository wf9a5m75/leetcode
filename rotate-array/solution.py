class Solution:
    def flip(self, nums: List[int], L: int, R: int) -> None:
        while(L < R):
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        N = len(nums)
        k = k % N
        if (k == 0):
            return

        # Flip (reverse) the array
        self.flip(nums, 0, N - 1)

        # Flip partially
        self.flip(nums, 0, k - 1)
        self.flip(nums, k, N - 1)



    def rotate_passed_but_entry_level(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k % N
        if (k == 0):
            return


        for i, val in enumerate(nums[N - k:] + nums[:N - k]):
            nums[i] = val
