class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            hash_map.setdefault(nums[i], 0)
            hash_map[nums[i]] += 1
        return list(sorted(hash_map, key=lambda x: hash_map[x], reverse=True)[:k])
