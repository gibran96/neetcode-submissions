class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i,n in enumerate(nums):
            res = target - n
            if res in prevMap:
                return [prevMap[res], i]
            prevMap[n] = i