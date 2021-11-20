class Solution:
    def backtrack(self, arr, soFar, curr, remainLEDs, threshold, allowRemainLEDs):
        if remainLEDs == 0:
            return [soFar.copy()]

        s = soFar[0]
        results = []
        for i in range(curr + 1, len(arr)):
            if (s + arr[i] <= threshold):
                soFar[0] += arr[i]
                soFar[1] += 1

                others = self.backtrack(arr, soFar, i, remainLEDs - 1, threshold, allowRemainLEDs)

                soFar[0] -= arr[i]
                soFar[1] -= 1

                for other in others:
                    results.append(other)

        if allowRemainLEDs:
            results.append(soFar.copy())

        return results

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn == 0:
            return ["0:00"]

        hours = [1, 2, 4, 8]
        minutes = [1, 2, 4, 8, 16, 32]

        hourPairs = self.backtrack(hours, [0, 0], -1, turnedOn, 11, True)
        # print(hourPairs)

        results = []
        for h, hLen in hourPairs:
            if (turnedOn - hLen > 0):
                minutePairs = self.backtrack(minutes, [0, 0], -1, turnedOn - hLen, 59, False)
                for mPair in minutePairs:
                    results.append("{}:{:02d}".format(h, mPair[0]))
            else:
                results.append("{}:00".format(h))
        # results.sort()

        return results
