class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        m = set()
        l, ans = 0, 0
        for i in range(len(s)):
            while s[i] in m:
                m.remove(s[l])
                l += 1
            else:
                m.add(s[i])
                ans = max(ans, i - l + 1)
        return ans