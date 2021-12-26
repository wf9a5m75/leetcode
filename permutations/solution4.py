class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:

		def recursion(arr: List[int], prevResults: List[List[int]]) -> List[List[int]]:
			# Processed all elements
			N = len(arr)
			if (N == 0):
				return prevResults

			results = []
			for prev in prevResults:
				for i in range(len(prev) + 1):
					results += [prev[:i] + [arr[0]] + prev[i:]]
			return recursion(arr[1:], results)

		return recursion(nums, [ [] ])
