class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        list_1 = []
        for i in nums1:
            if i in nums2:
                list_1.append(i)
        return list_1