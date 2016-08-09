class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n == 0):
            return 0
        i = int(math.log(n,5))
        
        temp = [int(n/(5**k)) for k in range(1,i+1)]
        return sum(temp)