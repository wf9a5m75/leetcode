class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # M = len(text1)
        # N = len(text2)

        # Build a character to indicies map.
        #    O(M)
        imap2 = defaultdict(list)
        for i, case in enumerate(text1):
            imap2[case].append(-i)

        # Rebuild the text2 using binary search
        #   O(N log N)
        tail = []
        for case in text2[::-1]:
            for idx in imap2[case]:
                j = bisect_left(tail, idx)
                if j == len(tail):
                    tail.append(idx)
                else:
                    tail[j] = idx

        return len(tail)
                    
