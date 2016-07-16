class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        lenth = len(s)
        number = 1
        reversed_string = ""
        while number <= lenth:
            reversed_string += s[-number]
            number += 1
        return reversed_string