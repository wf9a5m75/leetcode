class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0

        jmpCnt = nextJmp = currJmp = 0
        for i in range(N):
            nextJmp = max(nextJmp, i + nums[i])
            if i == currJmp:
                jmpCnt += 1
                currJmp = nextJmp
                if currJmp >= N - 1:
                    break
        return jmpCnt
                
