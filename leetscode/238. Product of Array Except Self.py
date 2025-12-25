class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n   # result array

        # Prefix pass (left products)
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Suffix pass (right products)
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
