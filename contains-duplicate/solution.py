class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] == nums[i]:
                return True
        return False

    def containsDuplicate_easy(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    def containsDuplicate(self, nums: List[int]) -> bool:
        mem = set()
        for n in nums:
            if n in mem:
                return True
            mem.add(n)
        return False
