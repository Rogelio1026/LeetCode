class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a*b<0 and abs(min(a,b))<abs(max(a,b)):
            a=~a
            b=~b
            while (a & b) != 0:
                c = (a & b) << 1
                b = a ^ b
                a = c
            return ~(a | b)-1
        elif a*b<=0 and abs(a)==abs(b):
            return 0
        else:
            while (a & b) != 0:
                c = (a & b) << 1
                b = a ^ b
                a = c
            return a | b