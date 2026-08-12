class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        for c in s:
            sMap[c] = 1 + sMap.get(c, 0)
        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)
        return sMap == tMap