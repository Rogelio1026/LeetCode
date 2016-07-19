class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        i=l-1
        n=nums.count(0)
        while i>=0:
            if nums[i]==0:
                del nums[i]
            i-=1
        list_1=[0]*n
        return nums.extend(list_1)