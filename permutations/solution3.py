class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		def backtrack(arr: List[int]) -> List[List[int]]:
			N = len(arr)
			if (N == 1):
				return [arr]

			results = []
			for i in range(N):
				others = backtrack(arr[:i] + arr[i + 1:])
				for other in others:
					other.insert(0, arr[i])
				results += others

			return results

		N = len(nums)
		if (N == 1):
			return [nums]

		# We generate the permutation for the first element
		results = backtrack(nums[1:])

		# Add the nums[0]
		M = len(results)
		for i in range(M):
			results[i].insert(0, nums[0])

		# For nums[1] to nums[N - 1],
		# we copy the previous result, then rotate it

		for i in range(1, N):
			for j in range(M):
				result = results[-M].copy()
				result.append(result.pop(0))
				results.append(result)
		return results
