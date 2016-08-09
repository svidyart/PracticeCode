class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if(not num):
            return 0
        a = num%9
        if(a):
            return a
        return 9