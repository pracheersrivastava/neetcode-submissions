class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = {}
        for i in range(len(nums)):
            hashset[nums[i]] = hashset.get(nums[i], 0)+1
        for value in hashset.values():
            if value > 1:
                return True
        return False