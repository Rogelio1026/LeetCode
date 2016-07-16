class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = num
        list_1 = []
        list_2 = []
        if num > 9:
            num_str = str(num)
            list_1 = list(num_str)
            for i in list_1:
                i = int(i)
                list_2.append(i)
            print(list_2)
            a = sum(list_2)
            num = a
        return a