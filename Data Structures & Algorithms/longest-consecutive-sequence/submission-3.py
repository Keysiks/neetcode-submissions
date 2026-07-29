class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        m = set(nums)
        ans = 1
        for num in nums:
            if num - 1 not in m:
                c = 1
                while num + c in m:
                    m.remove(num + c)
                    c += 1
                    ans = max(ans, c)
                    
        return ans