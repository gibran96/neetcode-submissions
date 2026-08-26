class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean_s = "".join(c for c in s if c.isalnum()).lower()
        # s1 = clean_s[::-1]
        # return s1 == clean_s

        # two pointer
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
        