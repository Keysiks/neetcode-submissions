class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
        for s in strs:
            key = "".join(sorted(s))
            value = word_map.setdefault(key, [])
            word_map[key].append(s)
        return [value for value in word_map.values()]
