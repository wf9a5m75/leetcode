class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		results = []

		def dfs(arr: List[int], path: List[int]):
			N = len(arr)

			# Reached to the last element
			if (N == 1):
				results.append(path.copy())
				return

			# Pick one element, and record it on the path
			for i in range(N):
				path.append(nums.pop(i))
				self.permute(nums, path)
				nums.insert(i, path.pop())

		dfs(nums, [])
		return results
