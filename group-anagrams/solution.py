from collections import Counter
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = defaultdict(list)
        for word in strs:
            key = word
            key = "".join(sorted(word))
            mem[key].append(word)

        results = []
        for wkey in mem:
            results.append(mem[wkey])

        return results

    def groupAnagrams_slow(self, strs: List[str]) -> List[List[str]]:
        def myConvert(txt):
            countDic = Counter(txt)
            chars = list(countDic.keys())
            chars.sort()
            zipWord = []
            for c in chars:
                zipWord.append("{}{}".format(c, countDic[c]))
            return (txt, "".join(zipWord))

        strs = list(map(myConvert, strs))
        mem = defaultdict(list)
        for wdata in strs:
            key = wdata[1]
            mem[key].append(wdata[0])

        results = []
        for wkey in mem:
            results.append(mem[wkey])

        return results
