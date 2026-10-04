class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, c in enumerate(nums):
            left = target - nums[i]
            if left in hashmap:
                return [hashmap[left], i]
            else:
                hashmap[c] = i
