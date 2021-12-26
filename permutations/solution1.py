
class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		N = len(nums)

		# If no other combination, then goes back.
		if (N == 1):
			return [ nums.copy() ]

		results = []
		for i in range(N):
			# Pop one element from nums,
			# and we produce all combinations with the rest of the nums.
			tmp = nums.pop(i)
			others = self.permute(nums)

			# Inserting the one element we popuped into the other results
			for other in others:
				other.insert(0, tmp)
				results.append(other)

			# Put back the element
			nums.insert(i, tmp)
		return results
