class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            res = target - nums[i]
            if res in nums and nums.index(res) != i:
                return sorted([i, nums.index(res)])