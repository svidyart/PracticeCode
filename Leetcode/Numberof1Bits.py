class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ctr = 0
        while(n>0):
            ctr+=(n%2)
            n /= 2
        return ctr
        