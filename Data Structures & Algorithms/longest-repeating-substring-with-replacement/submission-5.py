class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {s[0]: 1}
        l, r = 0, 0
        maxx = 0
        while r < len(s):
            if r - l + 1 - max(freq.values()) <= k:
                maxx = max(maxx, r - l + 1)
                r += 1
                if r < len(s):
                    freq[s[r]] = freq.get(s[r], 0) + 1
            else:
                freq[s[l]] -= 1
                l += 1
        return maxx