# https://leetcode.com/problems/find-the-duplicate-number/solution/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p1 = p2 = nums[0]
        while(True):
            p1 = nums[p1]
            p2 = nums[nums[p2]]
            if p1 == p2:
                break

        p1 = nums[0]
        while(p1 != p2):
            p1 = nums[p1]
            p2 = nums[p2]
        return p1
