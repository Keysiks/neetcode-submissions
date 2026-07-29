class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash, t_hash = {}, {}
        for i in range(len(s)):
            s_hash.setdefault(s[i], 0)
            s_hash[s[i]] += 1
        for i in range(len(t)):
            t_hash.setdefault(t[i], 0)
            t_hash[t[i]] += 1

        return s_hash == t_hash