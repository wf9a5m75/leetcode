class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.append(100000000000)
        N = len(nums)
        p1 = p2 = 0
        cnt = 1
        while(p2 < N):
            if (nums[p2 - 1] == nums[p2]):
                if (cnt == 2):
                    p2 += 1
                else:
                    nums[p1] = nums[p2]
                    p1 += 1
                    p2 += 1
                    cnt += 1
            else:
                nums[p1] = nums[p2]
                p1 += 1
                p2 += 1
                cnt = 1
        return p1 - 1
