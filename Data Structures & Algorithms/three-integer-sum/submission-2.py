class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans: set[tuple[int]] = set()
        for i in range(len(nums)):
            l, r = 0, len(nums) - 1
            while l + 1 < r:
                if nums[l] + nums[r] == -nums[i] and len(set([i, l, r])) == 3:
                    ans.add(tuple(sorted([nums[l], nums[r], nums[i]])))
                    l += 1
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                else:
                    r -= 1
        return [list(m) for m in ans]