"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""

class Solution:
    def binarySearch(self, customfunction: 'CustomFunction', z: int, x: int) -> List[int]:
        leftY = 1
        rightY = 1000

        while(leftY != rightY):
            midY = (leftY + rightY) >> 1
            res = customfunction.f(x, midY)
            if (res == z):
                return midY
            elif (res < z):
                leftY = midY + 1
            else:
                rightY = midY
        return -1

    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []

        for x in range(1, 1000):

            res = self.binarySearch(customfunction, z, x)
            if (res != -1):
                ans.append([x, res])

        return ans
