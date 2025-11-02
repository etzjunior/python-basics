class Solution(object):
    def intersection(self, nums1, nums2):
        store = []
        for i in nums1:
            for j in nums2:
                if i == j:
                    store.append(i)
        return list(set(store))
