class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        list = [0]*(num+1)
        print (list)
        for n in range(1,num+1):
            if n%2:
                list[n]=list[n/2]+1
            else:
                list[n]=list[n/2]
        return list
        # time complexity O(n)
        # space complexity O(n)