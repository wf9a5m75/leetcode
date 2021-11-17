class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        lefts = {0: -1}
        ans = status = 0
        for i, char in enumerate(s):
            if char in vowels:
                status ^= vowels[char]
                if status not in lefts:
                    lefts[status] = i
            ans = max(ans, i - lefts[status])

        return ans
