class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # https://leetcode.com/problems/4sum/solution/

        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            results = []

            if len(nums) == 0:
                return results

            # There are k remaining values to add to the sum.
            # The average of these values is at least target

            average_value = target // k

            # we can not obtain a sum of target if the smallest value
            # in nums is greater than target.
            if average_value < nums[0] or nums[-1] < average_value:
                return results

            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        results.append([nums[i]] + subset)
            return results

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            results = []
            s = set()

            for i in range(len(nums)):
                if (len(results) == 0) or (results[-1][1] != nums[i]):
                    if (target - nums[i]) in s:
                        results.append([target - nums[i], nums[i]])
                s.add(nums[i])
            return results
        nums.sort()
        return kSum(nums, target, 4)

    def fourSum_two_pointers(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)

        mem = set()
        results = []
        for a in range(N - 4 + 1):
            for b in range(a + 1, N - 3 + 1):
                L = b + 1
                R = N - 1

                target2 = target - nums[a] - nums[b]

                while(L != R):
                    s = nums[L] + nums[R]
                    if (s > target2):
                        R -= 1
                    elif (s == target2):
                        if (L != R):
                            key = "{}:{}:{}:{}".format(nums[a], nums[b], nums[L], nums[R])
                            if key not in mem:
                                results.append((nums[a], nums[b], nums[L], nums[R]))
                                mem.add(key)
                        L += 1
                    else:
                        L += 1
        return results



        
