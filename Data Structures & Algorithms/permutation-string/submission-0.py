class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        letters1 = {chr(ord("a") + i): 0 for i in range(26)}
        letters2 = {chr(ord("a") + i): 0 for i in range(26)}
        k, n = len(s1), len(s2)

        for c in s1:
            letters1[c] += 1
        for c in s2[:k]:
            letters2[c] += 1

        match = sum([letters1[chr(ord("a") + i)] == letters2[chr(ord("a") + i)] for i in range(26)])
        if match == 26:
            return True

        for i in range(k, n):
            letters2[s2[i - k]] -= 1
            letters2[s2[i]] += 1
            match = sum([letters1[chr(ord("a") + i)] == letters2[chr(ord("a") + i)] for i in range(26)])
            if match == 26:
                return True
        return False




