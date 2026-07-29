class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            hash_map.setdefault(nums[i], 0)
            hash_map[nums[i]] += 1
        heap = []
        for num in hash_map.keys():
            heapq.heappush(heap, (hash_map[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
