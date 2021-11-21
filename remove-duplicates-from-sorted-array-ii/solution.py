class Solution:
    def removeDuplicates_another(self, nums: List[int]) -> int:
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
