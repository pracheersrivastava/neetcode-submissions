class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        ans = []
        for key, value in sorted_items[:k]:
            ans.append(key)

        return ans