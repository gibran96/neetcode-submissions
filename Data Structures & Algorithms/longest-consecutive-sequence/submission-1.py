class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # res = 0
        # numSet = set(nums)
        # for n in nums:
        #     temp = 0
        #     curr = n
        #     while curr in numSet:
        #         temp += 1
        #         curr += 1
        #     res = max(res, temp)
        # return res

        if not nums:
            return 0
        nums.sort()
        res = 0
        curr = nums[0]
        temp = 0
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                temp = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            temp += 1
            curr += 1
            res = max(res, temp)
        return res


            
                