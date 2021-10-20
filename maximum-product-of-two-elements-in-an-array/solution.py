class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # heap sort:
        #  ave: O(n log k)
        #     k denotes the number of kinds
        #
        #  worst-case: O(n log n)
        #     the case of all elements are unique
        heapq.heapify(nums)
        top2 = heapq.nlargest(2, nums)
        return (top2[0] - 1) * (top2[1] - 1)

    def maxProduct_normal_using_quicksort(self, nums: List[int]) -> int:

        # quick sort:
        #  ave: O(n log n)
        #
        #  worst-case: O(n**2)
        #     the array is already sorted
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
