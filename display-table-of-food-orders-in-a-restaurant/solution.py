class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foodItems = set()
        table = {}
        for cName, tableNum, foodItem in orders:
            foodItems.add(foodItem)
            if (tableNum not in table):
                table[tableNum] = defaultdict(int)
            table[tableNum][foodItem] += 1

        tableNums = sorted(table.keys(), key=int)
        foodItems = sorted(list(foodItems))

        results = []
        header = foodItems.copy()
        header.insert(0, "Table")
        results.append(header)

        for tableNum in tableNums:
            row = [str(tableNum)]
            for foodItem in foodItems:
                cnt = "0"
                if (foodItem in table[tableNum]):
                    cnt = str(table[tableNum][foodItem])
                row.append(cnt)
            results.append(row)
        return results
