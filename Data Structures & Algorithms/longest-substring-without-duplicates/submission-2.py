class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # res = 0
        # for l in range(len(s)):
        #     temp = set()
        #     temp.add(s[l])
        #     res = max(res, len(temp))
        #     r = l + 1
        #     while r < len(s):
        #         if s[r] not in temp:
        #             temp.add(s[r])
        #             res = max(res, len(temp))
        #         else:
        #             l = r
        #             break
        #         r += 1
        # return res
        temp = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in temp:
                temp.remove(s[l])
                l += 1
            temp.add(s[r])
            res = max(res, r - l + 1)
        return res

