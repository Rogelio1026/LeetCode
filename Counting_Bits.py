class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        list = [0]
        for n in range(1,num+1):
            power = 0
            while n >= 2**power:
                power += 1
            power -= 1
            count = 0
            while n > 0:
                if n >= 2**power:
                    n -= 2**power
                    count += 1
                    power -= 1
                else:
                    power -=1
            list.append(count)
        return list