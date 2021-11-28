class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #
        # hash approach
        #   time complexity: O(N)
        #   space complexity: O(N)
        
        mem = {}
        for i, val in enumerate(nums):
            if (val in mem) and (i - mem[val] <= k):
                return True
            mem[val] = i
        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #
        # sliding window approach
        #   time complexity: O(N)
        #   space complexity: O(k)

        N = len(nums)
        mem = set()
        for i in range(N):
            if i - k - 1 >= 0:
                mem.remove(nums[i - k - 1])

            if nums[i] in mem:
                return True
            mem.add(nums[i])
        return False
