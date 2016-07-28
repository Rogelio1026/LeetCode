class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {}
        list = []
        for n in nums:
            if n not in dict:
                dict[n]=1
            else:
                dict[n]=2
        for n in dict:
            if dict[n]==1:
                list.append(n)
        return list
        # time - O(n)
        # space - O(n)