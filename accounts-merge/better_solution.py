class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        N = len(accounts)
        parents = [0] * N
        parent2name = {}

        def findParent(idx):
            while(parents[idx] != idx):
                idx = parents[idx]
            return idx

        # email -> parentId
        seen = {}
        for i, account in enumerate(accounts):
            parents[i] = i
            parent2name[i] = account[0]

            M = len(account)

            for j in range(1, M):
                email = account[j]
                if (email in seen):
                    # If the email has already another parent,
                    # connect current parent to the other parent
                    parent1 = findParent(seen[email])
                    parent2 = findParent(parents[i])
                    parents[parent2] = parent1
                else:
                    seen[email] = parents[i]

        # Create results
        id2emails = defaultdict(list)
        for email in seen.keys():
            parentId = findParent(seen[email])
            id2emails[parentId].append(email)

        results = []
        for parentId in id2emails.keys():
            result = sorted(id2emails[parentId])
            result.insert(0, parent2name[parentId])
            results.append(result)

        return results
