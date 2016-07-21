class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        list_1 = []
        l = len(nums)
        i = 0
        while i<l-1:
            if nums[i] != nums[i+1]:
                list_1.append(nums[i])
                i+=1
            else:
                i+=2
        if i==l-1:
            list_1.append(nums[i])
        return list_1