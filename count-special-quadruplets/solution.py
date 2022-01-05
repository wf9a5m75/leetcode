class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0
        N = len(nums)

        count = {}

        # The first "d-c" set
        count[nums[N-1] - nums[N-2]] = 1
        # print(count)

        for b in range(N - 3, 0, -1):
            for a in range(b - 1, -1, -1):
                a_and_b = nums[a] + nums[b]
                ans += count.get(a_and_b, 0)

            for d in range(N - 1, b, -1):
                # Assuming "c" as "b"
                d_minus_c = nums[d] - nums[b]
                count[d_minus_c] = count.get(d_minus_c, 0) + 1

            # print(count)
        return ans
