class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        N = len(arr)

        threshold *= k
        ans = 0
        sumWindow = sum(arr[0:k])
        if (sumWindow >= threshold):
            ans += 1

        L = 1
        R = k
        while(R < N):
            sumWindow = sumWindow - arr[L - 1] + arr[R]
            if (sumWindow >= threshold):
                ans += 1
            L += 1
            R += 1
        return ans



    def numOfSubarrays_another(self, arr: List[int], k: int, threshold: int) -> int:
        arr = list(map(lambda x: x / k, arr))

        L = 1
        R = k
        N = len(arr)
        ave = sum(arr[0:k])
        ans = 1 if ave >= threshold else 0
        # print(ave, " : ", arr[0:k])

        while(R < N):
            ave = ave - arr[L - 1] + arr[R]
            # print(ave, " : ", arr[L:R + 1])

            ans += 1 if ave >= threshold else 0
            L += 1
            R += 1
        return ans
