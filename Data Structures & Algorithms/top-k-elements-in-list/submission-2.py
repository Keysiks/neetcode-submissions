class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            hash_map[nums[i]] = 1 + hash_map.get(nums[i], 0)
        for num, cnt in hash_map.items():
            freq[cnt].append(num)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            c = freq[i]
            for num in c:
                res.append(num)
                if len(res) == k:
                    return res