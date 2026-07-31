class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:                 # левая половина отсортирована
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1                      # target внутри неё
                else:
                    lo = mid + 1                      # значит в другой
            else:                                     # правая половина отсортирована
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1