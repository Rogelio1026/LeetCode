class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        list_1 = []
        list_a = []
        list_b = []
        list_c = []
        c = min(a,b)
        c = str(c)
        list_c.append(c[0])
        for i in range(abs(a)):
            list_a.append(i)
        for j in range(abs(b)):
            list_b.append(j)
        if a*b >= 0:
            list_1.extend(list_a)
            list_1.extend(list_b)
            if a>0 or b>0:
                return len(list_1)
            elif a==0 and b==0:
                return 0
            else:
                list_c.append(str(len(list_1)))
                return int("".join(list_c))
        else:
            for x in max(list_a,list_b):
                if x not in min(list_a,list_b):
                    list_1.append(x)
            if (a > b and abs(a) > abs(b)) or (b > a and abs(b) > abs(a)):
                return len(list_1)
            else:
                list_c.append(str(len(list_1)))
                return int("".join(list_c))