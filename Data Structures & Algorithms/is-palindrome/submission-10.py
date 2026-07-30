class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ""
        for symbol in s:
            new_s += symbol if symbol.isdigit() or symbol.isalpha() else ""
        return new_s == new_s[::-1]
