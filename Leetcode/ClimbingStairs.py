class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.d = {}
        self.d[0] = 1
        self.d[1] = 1
        for i in range(2,n+1):
            self.d[i] = self.d[i-1] + self.d[i-2]
        return self.d[n]
        
        