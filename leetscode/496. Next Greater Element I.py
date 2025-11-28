class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        results = []
        for i in nums1:
            index = nums2.index(i)
            next_greater = -1
            for j in range(index+1, len(nums2)):
                if nums2[j] > i:
                    next_greater = nums2[j]
                    break
            results.append(next_greater)
        return results