def runningSum(self, nums):
        sums = []
        for i in range(len(nums)):
            if i == 0:
                sums.append(nums[i])
            else:
                nums[i] += nums[i-1]
                sums.append(nums[i])
        return sums