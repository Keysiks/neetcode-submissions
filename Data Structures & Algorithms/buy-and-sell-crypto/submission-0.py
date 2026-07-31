class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minn = prices[0]
        for i in range(1, len(prices)):
            minn = min(prices[i - 1], minn)
            ans = max(ans, prices[i] - minn)
        return ans