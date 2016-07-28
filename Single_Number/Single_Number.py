class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict={}
        for n in nums:
            if n not in dict:
                dict[n]=1
            else:
                dict[n]=2
        for n in dict:
            if dict[n] == 1:
                return n
        # time - O(n)
        # space - O(n)