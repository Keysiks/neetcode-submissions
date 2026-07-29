class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            hash_map.setdefault(nums[i], target - nums[i]) 
        for key, value in hash_map.items():
            if value in hash_map:
                if key == value:
                    ans = []
                    c = 0
                    for i in range(len(nums)):
                        if nums[i] == key:
                            c += 1
                            ans.append(i)
                        if c == 2:
                            return ans
                    continue
                return [nums.index(key), nums.index(value)]