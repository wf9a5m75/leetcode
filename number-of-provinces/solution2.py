class Solution:
    def findParent(self, provinces: dict, city: int) -> int:
        if city not in provinces:
            return -1
        while(provinces[city] != city):
            city = provinces[city]
        return city
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = {}
        provIdx = 201
        N = len(isConnected)

        ans = 0
        for currCity, conn in enumerate(isConnected):

            # If the currentCity belongs a province,
            # get the index. If not, obtain a new province ID.
            currCityRoot = self.findParent(provinces, currCity)
            if currCityRoot == -1:
                provinces[currCity] = currCity
                currCityRoot = currCity


            cities = []
            for i in range(N):
                if i == currCity:
                    continue

                # If we find a connected city,
                # get the province ID of the other city,
                # and union with the currentCity
                if conn[i] == 1:
                    otherProvId = self.findParent(provinces, i)
                    if otherProvId == -1:
                        provinces[i] = currCityRoot
                    else:
                        # Union two provinces
                        provinces[provIdx] = provIdx
                        provinces[currCityRoot] = provIdx
                        provinces[otherProvId] = provIdx
                        provIdx += 1
        ans = 0
        checked = set()
        for i in range(N):
            root = self.findParent(provinces, i)
            if root not in checked:
                checked.add(root)
                ans += 1
        return ans
