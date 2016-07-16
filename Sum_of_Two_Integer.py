class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        list = []
        for i in range(a):
            list.append(i)
        for j in range(b):
            list.append(j)
        return len(list)