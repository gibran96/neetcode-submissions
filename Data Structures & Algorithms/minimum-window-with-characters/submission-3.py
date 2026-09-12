class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if not t:
        #     return ""
        # wCount = {}
        # tCount = {}
        # for c in t:
        #     tCount[c] = 1 + tCount.get(c, 0)
        # res = [-1, -1]
        # resLen = float("infinity")
        # for i in range(len(s)):
        #     sCount = {}
        #     for j in range(i, len(s)):
        #         sCount[s[j]] = 1 + sCount.get(s[j], 0)
        #         flag = True
        #         for c in tCount:
        #             if tCount[c] > sCount.get(c, 0):
        #                 flag = False
        #                 break
        #         if flag and (j - i + 1) < resLen:
        #             resLen = j - i + 1
        #             res = [i, j]
        # l, r = res
        # return s[l : r + 1] if resLen != float("infinity") else ""
        if not t:
            return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

        
            