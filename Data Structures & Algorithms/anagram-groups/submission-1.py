class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aGroup = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key not in aGroup:
                aGroup[key] = []
            aGroup[key].append(s)
        return list(aGroup.values())

