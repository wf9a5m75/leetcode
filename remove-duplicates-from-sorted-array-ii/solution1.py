class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)

        L = 1
        R = N
        cnt = 1
        while(L < R):
            if nums[L - 1] == nums[L]:
                if cnt + 1 == 3:
                    nums.append(nums.pop(L))
                    R -= 1
                else:
                    cnt += 1
                    L += 1
            else:
                cnt = 1
                L += 1
        return R
