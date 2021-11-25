class Solution:
    def numSubarrayProductLessThanK_editorial(self, nums: List[int], k: int) -> int:
        if (k < 2):
            return 0

        prod = 1
        ans = L = 0
        for R, val in enumerate(nums):
            prod *= val
            while(prod >= k):
                prod /= nums[L]
                L += 1
            ans += R - L + 1
        return ans

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if (k < 2):
            return 0

        # Since we calculate the number of subarray when (prod >= k),
        # the prod must over k at the last.
        nums.append(k + 1)

        N = len(nums)
        dup = ans = 0

        # Ignore the numbers greater than or equal k.
        L = 0
        while(nums[L] >= k):
            L += 1
        R = L
        prod = 1

        while(R < N):
            prod *= nums[R]

            # If prod becomes greater than or equal k,
            # we calculate the number of subarray.
            if (prod >=  k):
                # print("L({}) , R({})".format(L, R), nums[L:R + 1])

                # The number of subarray is summation
                s = (R - L)
                s = (s * (s + 1)) // 2
                # print("--> s = ", s, nums[L:R])

                # The dup holds the number of duplicates last range.
                ans += s - dup

                # Move L
                while(L < R) and (prod >= k):
                    prod /= nums[L]
                    L += 1

                if (L == R):
                    # If L reaches to R, the nums[R] is also greater than or qual k.
                    # In that case, we need to find new start position.
                    while(L < N) and (nums[L] >= k):
                        L += 1
                    R = L
                    prod = 1
                    dup = 0
                else:
                    # The current range overlaps to the next subarray range.
                    # Reduces the number of duplicates when we calculate next time.
                    dup = (R - L)
                    dup = (dup * (dup + 1)) // 2
                    prod /= nums[R]
            else:
                R += 1

        return ans
