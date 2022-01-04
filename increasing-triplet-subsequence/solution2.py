class Solution:
    def increasingTriplet(self,nums):
        #
        # O(N) times, O(1) space
        #
        INF = float('inf')
        firstLowest = secondLowest = middle = INF
        for num in nums:
            if num <= firstLowest:
                if middle != INF:
                    secondLowest = firstLowest
                firstLowest = num
            elif num <= middle:
                middle = num
            else:
                # case1: [5,1,2,6]
                if (firstLowest < middle) and (secondLowest == INF):
                    print("case1", firstLowest, middle, num)

                # case2: [1,2,0,6]
                elif (secondLowest < middle):
                    print("case2", secondLowest, middle, num)
                return True
        return False
