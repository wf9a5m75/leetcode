class TrieNode:
    def __init__(self):
        self.person = None
        self.children = {}
        self.word = ""

    def add(self, word: str, idx: int = 0):

        val = word[idx]
        if val not in self.children:
            self.children[val] = TrieNode()

        if (idx < len(word) - 1):
            return self.children[val].add(word, idx + 1)
        else:
            self.word = word
            return self

    def __repr__(self):
        return "{}{}".format(self.word, self.children)

class Person:
    def __init__(self, name: str):
        self.name = name
        self.emails = []

    def __repr__(self):
        return "{}:{}".format(self.name, self.emails)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mgr = TrieNode()
        people = []

        for account in accounts:
            name = account.pop(0)
            unknown = []
            known = []
            for email in account:
                lastNode = mgr.add(email)
                if lastNode.person == None:
                    unknown.append(lastNode)
                else:
                    if (lastNode.person not in known):
                        known.append(lastNode.person)

            if (len(known) == 0):
                person = Person(name)
                people.append(person)
            else:
                # Union groups
                person = known.pop(0)

                for otherPerson in known:
                    person.emails += otherPerson.emails

                    for email in otherPerson.emails:
                        email.person = person

                    people.remove(otherPerson)

            for lastNode in unknown:
                lastNode.person = person
                person.emails.append(lastNode)


        results = []
        for person in people:
            result = set()
            for email in person.emails:
                result.add(email.word)
            result = sorted(list(result))
            result.insert(0, person.name)

            results.append(result)

        return results           
