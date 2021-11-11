class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        N = len(arr)
        arr.append(0)
        for length in range(1, N + 1, 2):
            i = 0
            s = sum(arr[:length])
            ans += s
            # print("---", length)
            # print(s)
            while(i + length < N):
                i += 1
                s = s - arr[i - 1] + arr[i + length - 1]
                # print(i, s)
                ans += s
        return ans
                
