import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = collections.defaultdict(list)
        res = []
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            freqMap[tuple(count)].append(s)

        for l in freqMap.values():
            res.append(l)
        return res


