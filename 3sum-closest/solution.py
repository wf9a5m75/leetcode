import random
class Solution:
    def quickSort(self, nums: List[int], start: int, end: int) -> None:
        if (start >= end):
            return
        L, R = start, end
        pivot = nums[random.randint(L, R)]
        while(L <= R):
            while(L < end) and (nums[L] < pivot):
                L += 1
            while(R > start) and (nums[R] > pivot):
                R -= 1
            if (L > R):
                break
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R -= 1
        if (start < R):
            self.quickSort(nums, start, R)
        if (L < end):
            self.quickSort(nums, L, end)

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N = len(nums)

        self.quickSort(nums, 0, N - 1)


        ans = 10 ** 5
        minDiff = 10 ** 5
        for i in range(N - 2):
            target2 = target - nums[i]
            j = i + 1
            k = N - 1

            while(j < k):
                s = nums[j] + nums[k]
                if (s == target2):
                    # nums[i] + nums[j] + nums[k] == target
                    return target
                diff = abs(target2 - s)
                if minDiff > diff:
                    ans = s + nums[i]
                    minDiff = diff

                if (s < target2):
                    j += 1
                else:
                    k -= 1
        return ans
