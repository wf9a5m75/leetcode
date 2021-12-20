class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pN = len(p)
        sN = len(s)
        if (pN > sN):
            return []

        results = []
        SATISFIED = 0
        for c in p:
            SATISFIED |= 1 << (ord(c)-97)

        pCounts = Counter(p)
        sCounts = defaultdict(int)

        flags = 0
        for j in range(pN):
            c = s[j]
            sCounts[c] += 1
            if (c in p):
                if (sCounts[c] >= pCounts[c]):
                    flags |= 1 << (ord(c) - 97)
        if (flags == SATISFIED):
            results.append(0)

        # print("[{}] {} {:03b}".format(0, s[0], flags), sCounts)
        i = 1
        while(i <= sN - pN):
            prev = s[i - 1]
            if (prev in pCounts):
                sCounts[prev] -= 1
                bitMask = 1 << (ord(prev) - 97)
                if (flags & bitMask > 0) and (sCounts[prev] < pCounts[prev]):
                    flags ^= bitMask

            c = s[i + pN - 1]
            if (c in pCounts):
                sCounts[c] += 1
                bitMask = 1 << (ord(c) - 97)
                if (flags & bitMask == 0) and (c in pCounts) and (sCounts[c] >= pCounts[c]):
                    flags |= bitMask

            # print("[{}] {} ({}) {:03b}".format(i, s[i:i+pN], c, flags), sCounts)
            if (flags == SATISFIED):
                results.append(i)

            i += 1
        return results
            
