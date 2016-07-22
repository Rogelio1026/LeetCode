class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if abs(a) == abs(b) and a * b <= 0:
            return 0
        else:
            while (a & b) != 0:
                c = (a & b) << 1
                b = a ^ b
                a = c
            return a | b