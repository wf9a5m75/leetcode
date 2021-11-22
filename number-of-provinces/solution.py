class City:
    def __init__(self, label):
        self.label = label
        self.connected = []
        self.province = 0

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        cities = [City(i) for i in range(n)]

        pIdx = 0
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    isConnected[i][j] = 0
                    isConnected[j][i] = 0
                    cities[i].connected.append(j)
                    cities[j].connected.append(i)

        provinces = []
        for i, city in enumerate(cities):
            if cities[i].province == 0:
                connected = []
                queue = [i]
                pMax = 0
                while(queue):
                    c = queue.pop(0)
                    for other in cities[c].connected:
                        if (other not in connected):
                            pMax = max(pMax, cities[other].province)
                            connected.append(other)
                            queue.append(other)

                if pMax == 0:
                    provinces.append(connected)
                    label = len(provinces)
                    for c in connected:
                        cities[c].province = label
                        cities[c].connected = []

            # print(provinces)
        return len(provinces)
    
