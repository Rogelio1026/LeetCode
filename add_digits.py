class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = num
        list_1 = []
        while num > 9:
            num_str = str(num)
            list_1 = list(num_str)
            list_2 = []
            for i in list_1:
                i = int(i)
                list_2.append(i)
            a = sum(list_2)
            num = a
        return a