from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        #
        # Remainder + binary search
        #  time complexity : O(N log N)
        #  space complexity: O(N)
        #
        mem = defaultdict(list)
        for i, t in enumerate(time):
            t = t % 60
            mem[t].append(i)
            time[i] = t

        ans = 0
        for i, t in enumerate(time):
            if (t == 0):
                rest = 0
            else:
                rest = 60 - t
            if rest not in mem:
                continue

            indicies = mem[rest]
            N = len(indicies)
            L, R = 0, N
            target = i + 1
            while(L != R):
                mid = (L + R) >> 1
                if indicies[mid] == target:
                    L = mid
                    break
                elif (indicies[mid] < target):
                    L = mid + 1
                else:
                    R = mid
            ans += (N - L)
        return ans

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        #
        # Remainder counter approach
        #  time complexity : O(N)
        #  space complexity: O(N)
        #
        remainders = [0] * 60
        ans = 0
        for t in time:
            t = t % 60
            if (t == 0):
                ans += remainders[0]
            else:
                ans += remainders[60 - t]
            remainders[t] += 1
        return ans
