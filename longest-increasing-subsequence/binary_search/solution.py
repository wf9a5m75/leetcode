class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        NEG_INF = -10000000
        arr = [NEG_INF]
        for num in nums:
            if arr[-1] < num:
                arr.append(num)
            else:
                j = bisect_left(arr, num)
                arr[j] = num
        # print(arr)
        return len(arr) - 1
