class Solution:
    def compress(self, chars: List[str]) -> int:
        N = len(chars)
        i = j = 0
        while(i < N):
            cnt = 0
            while(i < N) and (chars[i] == chars[j]):
                i += 1
                cnt += 1

            # character
            j += 1

            # digits of the cnt
            if cnt > 1:
                for k in str(cnt):
                    chars[j] = k
                    j += 1
            if (i < N):
                chars[j] = chars[i]
        return j
