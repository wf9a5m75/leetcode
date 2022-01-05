class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n, n * 2):
            nums[i] = (nums[i] << 10) | nums[i - n]

        idx = 0
        for i in range(n, n * 2):
            nums[idx] = nums[i] & 1023
            nums[idx + 1] = nums[i] >> 10
            idx += 2

        return nums
