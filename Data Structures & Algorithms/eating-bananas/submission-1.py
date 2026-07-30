class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ceil(n: int, k: int) -> int:
            return n // k if n % k == 0 else n // k + 1
        if len(piles) == 1:
            return ceil(piles[0], h)
        l, r = 1, max(piles)
        while l + 1 < r:
            mid = (l + r) // 2
            eat = sum([ceil(piles[i], mid) for i in range(len(piles))])
            if eat <= h:
                r = mid
            else:
                l = mid
        return r