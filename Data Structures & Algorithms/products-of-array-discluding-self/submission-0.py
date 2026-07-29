class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        pref = [1] * (len(nums))
        post = [1] * (len(nums))
        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]
        return [post[i] * pref[i] for i in range(len(nums))]