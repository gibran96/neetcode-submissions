class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(c for c in s if c.isalnum()).lower()
        s1 = clean_s[::-1]
        return s1 == clean_s