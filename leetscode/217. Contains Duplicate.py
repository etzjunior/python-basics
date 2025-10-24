class Solution(object):
    def containsDuplicate(self, nums):
        tracker = []
        for x in nums:
            if x in tracker:
                return True 
            tracker.append(x)
        return False