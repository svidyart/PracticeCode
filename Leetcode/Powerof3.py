class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 0
        while(True):
            if(n==3**i):
                return True
            if(3**i < n):
                i += 1
            else:
                return False
