class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = []
        # for i in range(len(nums)):
        #     res = 1
        #     for j in range(len(nums)):
        #         if nums[j] == nums[i]:
        #             continue
        #         res = res * nums[j]
        #     output.append(res)
        # print(output)
        # return output
        l = len(nums)
        prefix = [0] * l
        suffix = [0] * l
        res = [0] * l
        prefix[0] = 1
        suffix[l - 1] = 1
        for i in range(1, l):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(l-2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        for i in range(l):
            res[i] = prefix[i] * suffix[i]
        return res