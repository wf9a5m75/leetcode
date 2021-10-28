class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
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



        
